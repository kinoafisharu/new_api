# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.db.models.base import ModelBase
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site as DjangoSite
from django.core import exceptions
import itertools as it
from functools import reduce
import logging

from base.models_dic import *
from base.models_choices import *
logger = logging.getLogger(__name__)



class Images(models.Model):
    file = models.CharField(max_length=256)
    status = models.CharField(max_length=1, choices=IMAGES_STATUS, verbose_name='Статус изображения')

class NamePerson(models.Model):
    '''
    Модель содержит имена персон
    1 - главное,
    2 - альтернативное,
    3 - в род.падеже,
    4 - на источнике
    '''
    status = models.IntegerField(verbose_name='Статус')
    language = models.ForeignKey(Language, null=True, on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Имя персоны')
    class Meta:
        verbose_name = u'Имя персоны'
        verbose_name_plural = u'Имена персон'
    def __unicode__(self):
        return '%s' % (self.name)


class Person(models.Model):
    '''
    Модель содержит данные персоны
    '''
    iid = models.BigIntegerField(verbose_name='Идентификатор персоны на imdb', blank=True, null=True)
    kid = models.BigIntegerField(verbose_name='Идентификатор персоны на киноафише', blank=True, null=True, db_index=True)
    male = models.IntegerField(verbose_name='Пол персоны', blank=True, null=True) # 1 - М, 2 - Ж
    name = models.ManyToManyField(NamePerson, verbose_name='Имя персоны')
    born = models.DateField(verbose_name='Дата рождения персоны', blank=True, null=True)
    country = models.ForeignKey(Country, verbose_name='Страна', blank=True, null=True, on_delete = models.PROTECT)
    city = models.ForeignKey(City, verbose_name='Город', blank=True, null=True, on_delete = models.PROTECT)

    artist = models.BooleanField(default=False)
    is_group = models.BooleanField(default=False)
    text = models.TextField(blank=True, null=True)
    musician = models.ManyToManyField("self", blank=True, null=True)
    poster = models.ManyToManyField(Images, verbose_name='Постеры, слайды', null=True)
    video = models.CharField(max_length=256, verbose_name='Видео', null=True, blank=True)
    class Meta:
        verbose_name = u'Персона'
        verbose_name_plural = u'Персоны'
    def __unicode__(self):
        return '%s' % (self.name)


class Interface(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name = 'IP адрес', blank=True, null=True)
    platform = models.CharField(max_length=64, verbose_name='Операционная система', blank=True, null=True)
    browser = models.CharField(max_length=64, verbose_name='Интернет браузер', blank=True, null=True)
    display = models.CharField(max_length=12, verbose_name='Разрешение экрана', blank=True, null=True)
    timezone = models.CharField(max_length=64, verbose_name='Часовой пояс', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Город', blank=True, null=True, on_delete = models.PROTECT)



class PersonInterface(models.Model):
    option1 = models.BooleanField(verbose_name='Настройка1 - slideblock_schedules', default=False)
    option2 = models.BooleanField(verbose_name='Настройка2', default=False)
    option3 = models.BooleanField(verbose_name='Настройка3', default=False)
    option4 = models.BooleanField(verbose_name='Настройка4', default=False)
    wf_topic = models.IntegerField(null=True)
    wf_last = models.IntegerField(null=True)
    wf_style = models.CharField(max_length=7, blank=True, null=True)
    wf_msg_open = models.BooleanField(default=False)
    first_change = models.BooleanField(verbose_name='Первое изменение настроек', default=False)
    changed = models.BooleanField(verbose_name='Изменения в настройках', default=False)
    likes = models.ManyToManyField('Likes')
    temp_subscription = models.IntegerField(verbose_name='KID', null=True)
    temp_subscription_topics = models.IntegerField(verbose_name='KID', null=True)
    money = models.FloatField(verbose_name='Счет', default=0)



class Accounts(models.Model):
    login = models.CharField(max_length=256, verbose_name='Логин (id или email)', blank=True, null=True)
    validation_code = models.CharField(max_length=256, verbose_name='Код авторизации', blank=True, null=True)
    email = models.CharField(max_length=256, verbose_name='email аккаунта, если есть', blank=True, null=True, db_index=True)
    auth_status = models.BooleanField(verbose_name='Авторизован ли по этому аккаунту', default=False)
    nickname = models.CharField(max_length=100, verbose_name='Никнэйм', blank=True, null=True)
    fullname = models.CharField(max_length=100, verbose_name='Имя Фамилия', blank=True, null=True)
    born = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    male = models.IntegerField(verbose_name='Пол', blank=True, null=True) # 1 - М, 2 - Ж
    avatar = models.CharField(max_length=128, verbose_name='Название аватарки', blank=True, null=True)

class Profile(models.Model):
    """
    Расширение модели User, дополнительные атрибуты
    """
    user = models.OneToOneField(User, on_delete = models.PROTECT)
    person = models.ForeignKey(Person, verbose_name='Персона', null=True, on_delete = models.PROTECT)
    personinterface = models.ForeignKey(PersonInterface, verbose_name='Личные настройки', null=True, on_delete = models.PROTECT)
    interface = models.ManyToManyField(Interface, verbose_name='Связь с интерфейсами')
    accounts = models.ManyToManyField(Accounts, verbose_name='Связь с аккаунтами')
    login_counter = models.IntegerField(verbose_name='Количество посещений в месяц', blank=True, null=True)
    auth_status = models.BooleanField(verbose_name='Авторизован по email/openid', default=False)
    folder = models.CharField(max_length=128, verbose_name='Название папки для профиля')
    site = models.ForeignKey(DjangoSite, on_delete = models.PROTECT)
    show_profile = models.CharField(max_length=1, choices=SHOW_PROFILE_CHOICES, default='1')
    path = models.CharField(max_length=256, verbose_name='урл на который юзер пришел и был зарегестрирован', blank=True, null=True)
    site_admin = models.ManyToManyField(DjangoSite, verbose_name='Сайты администрирования', related_name="site_admin", null=True)
    phone = models.CharField(max_length=64, verbose_name='Телефон', blank=True, null=True)
    phone_visible = models.BooleanField(verbose_name='Виден ли телефон', default=False)
    kid = models.IntegerField(verbose_name='KID', null=True, db_index=True)
    bg = models.CharField(max_length=64, verbose_name='Фон', blank=True, null=True)
    bg_url = models.CharField(max_length=256, verbose_name='URL Фон', blank=True, null=True)


class APILogger(models.Model):
    """
    Лог обращения к API
    """
    user = models.ForeignKey(User, verbose_name='Пользователь', null=True, on_delete = models.PROTECT)
    date = models.DateTimeField(verbose_name='Дата обращения к API', db_index=True)
    details = models.CharField(max_length=256, verbose_name='Описание')
    ip = models.GenericIPAddressField(verbose_name = 'IP адрес', db_index=True)
    method = models.CharField(max_length=32, verbose_name='Названия метода, дампа')
    event = models.IntegerField(verbose_name='Код события')


class NameDistributors(models.Model):
    '''
    Названия кинопрокатчиков
    '''
    status = models.IntegerField(verbose_name='Статус имени (1 - главное, 0 - альтернативное, 2 - очищенное)')
    language = models.ForeignKey(Language, blank=True, null=True, on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Название бренда')
    def __unicode__(self):
        return '%s' % (self.name)


class Distributors(models.Model):
    '''
    Кинопрокатчики России, Украины и Белоруси
    '''
    iid = models.BigIntegerField(verbose_name='Идентификатор прокатчика на imdb', blank=True, null=True)
    kid = models.BigIntegerField(verbose_name='Идентификатор прокатчика на киноафише', blank=True, null=True)
    name = models.ManyToManyField(NameDistributors, verbose_name='Название', related_name='distributors')
    country = models.ForeignKey(Country, verbose_name='Страна', blank=True, null=True, on_delete = models.PROTECT)
    #film = models.ManyToManyField(Films, verbose_name='Фильм', blank=True, null=True)
    usa = models.BooleanField(verbose_name='США', default=False)
    class Meta:
        verbose_name = u'Дистрибьютор'
        verbose_name_plural = u'Дистрибьюторы'
    def __unicode__(self):
        return '%s' % (self.name)


class NameFilms(models.Model):
    '''
    Названия фильмов
    '''
    status = models.IntegerField(verbose_name='Статус имени (1 - главное, 0 - альтернативное, 2 - очищенное)')
    language = models.ForeignKey(Language, blank=True, null=True, on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Название')
    def __unicode__(self):
        return '%s' % (self.name)

class FilmsReleaseDate(models.Model):
    release = models.DateField(verbose_name='Дата релиза')
    note = models.CharField(max_length=256, null=True, blank=True)
    format = models.CharField(max_length=1, choices=FILM_RELEASE_FORMAT, verbose_name='Формат релиза', null = True)
    country = models.ForeignKey(Country, on_delete = models.PROTECT, null = True)
    class Meta:
        ordering = ['-release',]

class ProductionsCo(models.Model):
    name = models.CharField(max_length=256, verbose_name='Компания призводитель')
    imdb_id = models.IntegerField(verbose_name='IMDb идентификатор', null=True)


class Films(models.Model):
    name = models.ManyToManyField(NameFilms, verbose_name='Название продукта', null = True)
    creators = models.ManyToManyField(Person, through='RelationFP', verbose_name='Ключевые создатели', related_name="key_creators_%(class)s", null=True)
    release = models.ManyToManyField(FilmsReleaseDate)
    country = models.ManyToManyField(Country)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    year = models.IntegerField(verbose_name='Год', null = True)
    note = models.TextField(verbose_name='Аннотация', blank=True, null=True)
    type = models.CharField(max_length=1, choices=FILM_TYPE_CHOICES, verbose_name='Тип фильма', null=True)
    runtime = models.IntegerField(verbose_name='Хронометраж', null=True)
    rated = models.IntegerField(verbose_name='Аудитория', null=True)
    budget = models.ForeignKey(Budget, verbose_name='Бюджет', null=True, on_delete = models.PROTECT)
    production = models.ManyToManyField(ProductionsCo, verbose_name='Компания призводитель')
    imdb_id = models.CharField(verbose_name='IMDb идентификатор', null=True, db_index=True, max_length = 200)
    imdb_rate = models.FloatField(verbose_name='IMDb рейтинг', null=True)
    imdb_votes = models.IntegerField(verbose_name='IMDb кол-во голосов', null=True)
    kid = models.IntegerField(verbose_name='ID киноафиши', null=True, db_index=True)
    distributor = models.ManyToManyField(Distributors, verbose_name='Дистрибьютор')
    images = models.ManyToManyField(Images, verbose_name='Постеры, слайды')
    generated = models.BooleanField(verbose_name='Сгенерирован юзером через кнопку', default=False)
    generated_dtime = models.DateTimeField(verbose_name='Дата, время генерации', null=True)
    site = models.CharField(max_length = 300, null = True)
    limits = models.CharField (max_length = 100, null = True)
    description = models.TextField(max_length = 3000, null = True)
    comment = models.TextField(max_length = 3000, null = True)

    #image_parameter = models.ForeignKey(ImageParameter, verbose_name='Изображение', blank=True, null=True, related_name="image_%(class)s")
    #sound_parameter = models.ForeignKey(SoundParameter, verbose_name='Звук', blank=True, null=True, related_name="sound_%(class)s")
    # Saving model instance to db if all the requirements are satisfie


class FilmsVotes(models.Model):
    kid = models.IntegerField(verbose_name='ID фильма на киноафише')
    user = models.ForeignKey(Profile, verbose_name='Юзер', on_delete = models.PROTECT)
    rate_1 = models.IntegerField()
    rate_2 = models.IntegerField()
    rate_3 = models.IntegerField()


class Likes(models.Model):
    evaluation = models.IntegerField(verbose_name='Идентификатор оценки пользователя')
    film = models.IntegerField(verbose_name='KID', db_index=True, null = True)
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата время лайка', null=True)
    filmobject = models.ForeignKey(Films, on_delete = models.CASCADE, null = True, related_name = 'votes')
    # Tie all like objects to films objects by kid
    @classmethod
    def tie_all_filmobjects(self):
        for item in filter(lambda x: isinstance(x.film, int), self.objects.all()):
                kid = item.film
                try:
                    obj = Films.objects.get(kid = kid)
                except exceptions.MultipleObjectsReturned:
                    obj = None
                except exceptions.ObjectDoesNotExist:
                    obj = None
                if obj:
                    item.filmobject = obj
                    item.save()



class RelationFP(models.Model):
    '''
    Модель описывает связь Персоны и фильма с указанием типа и статуса участия
    персоны в фильме
    '''
    person = models.ForeignKey(Person, on_delete = models.PROTECT)
    status_act = models.ForeignKey(StatusAct, on_delete = models.PROTECT)
    action = models.ForeignKey(Action, on_delete = models.PROTECT)
    films = models.ForeignKey(Films, on_delete = models.PROTECT, related_name = 'persons')
    class Meta:
        verbose_name = u'Персона фильма'
        verbose_name_plural = u'Персоны фильмов'
    def __unicode__(self):
        return '%s' % self.person.name


class ImportSources(models.Model):
    """
    Источники информации
    """
    url = models.URLField(max_length=256, verbose_name='url источника')
    source = models.CharField(max_length=64, verbose_name='Название источника')
    code = models.IntegerField(verbose_name='Код источника', blank=True, null=True)
    dump = models.CharField(max_length=64, verbose_name='Название для дампов', null=True)
    #priority = models.IntegerField(verbose_name='Приоритет')


class FilmsSources(models.Model):
    # связи с источниками
    id_films = models.ForeignKey(Films, verbose_name='КиноИнфо', on_delete = models.PROTECT, related_name = 'sources')
    source = models.ForeignKey(ImportSources, verbose_name='Источник', on_delete = models.PROTECT)
    id_films_sources = models.BigIntegerField(verbose_name='Фильм у источника')

class FilmsBudget(models.Model):
    kid = models.IntegerField(verbose_name='KID')
    budget = models.CharField(max_length=64, verbose_name='Бюджет')


class KIFilmRelations(models.Model):
    '''
    Связь источника с названием фильма
    '''
    kid = models.BigIntegerField(verbose_name='ID фильма у источника')
    name = models.ManyToManyField(NameFilms, verbose_name='Название фильма', blank=True, null=True)


class Logger(models.Model):
    text = models.CharField(max_length=256, verbose_name='text')
    url = models.URLField(max_length=256, verbose_name='url', blank=True, null=True)
    obj_name = models.CharField(max_length=256, verbose_name='объект возбудивший ошибку', blank=True, null=True)
    extra = models.CharField(max_length=256, verbose_name='дополнительное информационное поле', blank=True, null=True)
    # event # 1 - импорт из киноафиши, 2 - парсер sms.txt, 3 - импорт сенсов из источников
    event = models.IntegerField(verbose_name='Номер лога')
    code = models.IntegerField(verbose_name='Код события')


class AlterStreetType(models.Model):
   value =  models.ForeignKey(StreetType, verbose_name='Оригинальный тип улицы', on_delete = models.PROTECT)
   name =  models.CharField(max_length=256, verbose_name='Альтернативоный тип улицы', blank=True, null=True)
   class Meta:
       verbose_name = u'Тип улицы'
       verbose_name_plural = u'Типы улиц'
   def __unicode__(self):
       return '%s' % self.name


class Phone(models.Model):
    """
    Модель описывает телефоны
    """
    phone = models.CharField(max_length=64, verbose_name='Номер телефона', blank=True)
    phone_type = models.CharField(max_length=1, choices=PHONE_TYPE_CHOICES, verbose_name='Тип телефона (Касса, Автоответчик)', blank=True)
    def __unicode__(self):
        return '%s' % (self.phone)


class Site(models.Model):
    """
    Модель описывает сайты
    """
    url = models.URLField(blank=True)
    site_type = models.CharField(max_length=1, choices=SITE_TYPE_CHOICES, verbose_name='Тип сайта', blank=True)
    def __unicode__(self):
        return '%s' % (self.url)


class Cinema(models.Model):
    """
    Модель описывает кинотеатры
    """
    name = models.ManyToManyField(NameCinema, verbose_name='Название кинотеатара', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Город', on_delete = models.PROTECT)
    cinema_circuit = models.ForeignKey(CinemaCircuit, verbose_name='Сеть кинотеатров', null=True, on_delete = models.PROTECT)
    metro = models.ManyToManyField(Metro, verbose_name='Станция метро', null=True)
    street_type = models.ForeignKey(StreetType, verbose_name='Тип улицы', null=True, on_delete = models.PROTECT)
    street_name = models.CharField(max_length=64, verbose_name='Название улицы', blank=True, null=True)
    number_housing  = models.IntegerField(verbose_name='Номер корпуса', blank=True, null=True)
    number_hous  = models.CharField(max_length=16, verbose_name='Номер дома', blank=True, null=True)
    letter_housing = models.CharField(max_length=1, verbose_name='Буква корпуса', blank=True, null=True)
    zip = models.CharField(max_length=6, verbose_name='Почтовый индекс кинотеатра', blank=True, null=True)
    phone = models.ManyToManyField(Phone, verbose_name='Номер(а) телефона(ов)', null=True)
    site = models.ManyToManyField(Site, verbose_name='Сайт(ы)', null=True)
    opening = models.DateTimeField(verbose_name='Дата открытия', blank=True, null=True)
    note = models.TextField(verbose_name='Примечания', blank=True, null=True)
    code = models.IntegerField(db_index=True, verbose_name='Идентификатор киноафиши')
    class Meta:
        verbose_name = u'Кинотеатр'
        verbose_name_plural = u'Кинотеатры'
    def __unicode__(self):
        return '%s, %s, %s' % (self.name, self.street_name, self.number_hous)


class Hall(models.Model):
    """
    Модель описывает Залы
    """
    name = models.ManyToManyField(NameHall, verbose_name='Название зала', blank=True, null=True)
    number = models.IntegerField(verbose_name='Номер зала', blank=True, null=True)
    seats = models.IntegerField(verbose_name='Число мест в зале', blank=True, null=True)
    screen_size_w = models.IntegerField(verbose_name='Ширина экрана', blank=True, null=True)
    screen_size_h = models.IntegerField(verbose_name='Высота экрана', blank=True, null=True)
    image_format = models.CharField(max_length=1, choices=ASPECT_RATIO_CHOICES, verbose_name='Формат экрана', blank=True)
    sound_format = models.CharField(max_length=1, choices=SOUND_CHOICES, verbose_name='Формат звука', blank=True)
    cinema = models.ForeignKey(Cinema, verbose_name='Кинотеатр', on_delete = models.PROTECT)
    max_price = models.IntegerField(verbose_name='Максимальная цена билета', blank=True, null=True)
    min_price = models.IntegerField(verbose_name='Минимальная цена билета', blank=True, null=True)
    kid = models.IntegerField(db_index=True, verbose_name='Идентификатор киноафиши')
    def __unicode__(self):
        return '%s, %s' % (self.name, self.cinema.name)


class Demonstration(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    time = models.DateTimeField(verbose_name='Дата, время сеанса')
    place = models.ForeignKey(Hall, verbose_name='Место сеанса', on_delete = models.PROTECT)


class ScheduleRelations(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название фильма')
    kid = models.IntegerField(verbose_name='Идентификатор киноафиши')
    hall = models.ForeignKey(Hall, on_delete = models.PROTECT)
    dtime = models.DateTimeField(verbose_name='Дата, время сеанса')


class Articles(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название статьи')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', editable=False)
    text = models.TextField(verbose_name='Текст')
    site = models.ForeignKey(DjangoSite, on_delete = models.PROTECT)


'''
class Session(models.Model):
    demonstration = models.ForeignKey(Demonstration)
    number = models.PositiveIntegerField('Порядок в демонстрации')
    film = models.ManyToManyField(Films, verbose_name='Фильм(ы)')
    average_price = models.IntegerField(verbose_name='Средняя цена билета', blank=True, null=True)
    number_people = models.IntegerField(verbose_name='Число людей на сеансе', blank=True, null=True)
    def __unicode__(self):
        return '%s' % (self.demonstration)
'''
# связь не с фильмом, а с названием фильма (ТЕСТ)
class Session(models.Model):
    """
    Модель описывает Сеансы
    """
    demonstration = models.ForeignKey(Demonstration, on_delete = models.PROTECT)
    number = models.PositiveIntegerField('Порядок в демонстрации')
    film = models.ManyToManyField(NameFilms, verbose_name='Фильм(ы)')
    average_price = models.IntegerField(verbose_name='Средняя цена билета', blank=True, null=True)
    number_people = models.IntegerField(verbose_name='Число людей на сеансе', blank=True, null=True)
    def __unicode__(self):
        return '%s' % (self.demonstration)


class HallsSources(models.Model):
    # связи залов с источниками
    id_hall = models.ForeignKey(Hall, verbose_name='Зал', on_delete = models.PROTECT)
    source = models.ForeignKey(ImportSources, verbose_name='Источник', on_delete = models.PROTECT)
    url_hall_sources = models.URLField(max_length=256, verbose_name='url-hall')


class SourceCities(models.Model):
    source_id = models.CharField(max_length=256, verbose_name='ID источника')
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', on_delete = models.PROTECT)
    city = models.ForeignKey(City, verbose_name='Город', on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Название города у источника')
    name_alter = models.CharField(max_length=256, verbose_name='Альт. название города у источника', blank=True, null=True)


class SourceCinemas(models.Model):
    source_id = models.CharField(max_length=256, verbose_name='ID источника')
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', on_delete = models.PROTECT)
    city = models.ForeignKey(SourceCities, verbose_name='Город источника', on_delete = models.PROTECT)
    cinema = models.ForeignKey(Cinema, verbose_name='Кинотеатр', on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Название кинотеатра у источника')
    name_alter = models.CharField(max_length=256, verbose_name='Альтер. кинотеатра у источника', blank=True, null=True)
    address = models.CharField(max_length=256, verbose_name='Адрес кинотеатра у источника', blank=True, null=True)
    latitude = models.FloatField(verbose_name='Широта', blank=True, null=True)
    longitude = models.FloatField(verbose_name='Долгота', blank=True, null=True)


class SourceHalls(models.Model):
    source_id = models.CharField(max_length=256, verbose_name='ID источника')
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', on_delete = models.PROTECT)
    cinema = models.ForeignKey(SourceCinemas, verbose_name='Зал источника', on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Название зала у источника')
    name_alter = models.CharField(max_length=256, verbose_name='Альтер. зала у источника', blank=True, null=True)
    kid = models.IntegerField(verbose_name='KID зала')


class SourceFilms(models.Model):
    source_id = models.CharField(max_length=256, verbose_name='ID источника', db_index=True)
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Название фильма у источника')
    name_alter = models.CharField(max_length=256, verbose_name='Альтер. фильма у источника', blank=True, null=True)
    kid = models.IntegerField(verbose_name='KID фильма', null=True, db_index=True)
    year = models.IntegerField(verbose_name='Год выпуска фильма у источника', blank=True, null=True)
    imdb = models.CharField(max_length=64, verbose_name='IMDB фильма у источника', blank=True, null=True)
    text = models.TextField(verbose_name='Описание фильма', blank=True, null=True)
    extra = models.CharField(max_length=256, verbose_name='Дополнительные данные', blank=True, null=True)
    rel_profile = models.ForeignKey(Profile, verbose_name='Кто связал', null=True, on_delete = models.PROTECT)
    rel_dtime = models.DateTimeField(verbose_name='Когда связал', null=True)
    rel_double = models.BooleanField(verbose_name='Дубль', default=False)
    rel_ignore = models.BooleanField(verbose_name='Игнорировать', default=False, db_index=True)
    filmobject = models.ForeignKey(Films, on_delete = models.PROTECT, verbose_name = 'Фильм', null = True)
    @classmethod
    def tie_all_filmobjects(self):
        for item in filter(lambda x: isinstance(x.kid, int), self.objects.all()):
                kid = item.kid
                try:
                    obj = Films.objects.get(kid = kid)
                except exceptions.MultipleObjectsReturned:
                    obj = None
                except exceptions.ObjectDoesNotExist:
                    obj = None
                if obj:
                    item.filmobject = obj
                    item.save()


class SourceSchedules(models.Model):
    source_id = models.CharField(max_length=256, verbose_name='ID источника', db_index=True)
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', on_delete = models.PROTECT)
    film = models.ForeignKey(SourceFilms, verbose_name='Фильм источника', on_delete = models.PROTECT)
    cinema = models.ForeignKey(SourceCinemas, verbose_name='Кинотеатр источника', on_delete = models.PROTECT)
    dtime = models.DateTimeField(verbose_name='Дата и время сеанса', db_index=True)
    hall = models.IntegerField(verbose_name='KID зала', blank=True, null=True)
    #hall_obj = models.ForeignKey(SourceHalls, verbose_name='зал', null=True)
    sale = models.BooleanField(verbose_name='Возможность он-лайн покупки', default=False)
    price = models.CharField(max_length=64, verbose_name='Цена билета', blank=True, null=True)
    extra = models.CharField(max_length=256, verbose_name='Любой дополнительный параметр', null=True)

class SourceReleases(models.Model):
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', on_delete = models.PROTECT)
    film = models.ForeignKey(SourceFilms, verbose_name='Фильм источника', on_delete = models.PROTECT)
    release = models.DateField(verbose_name='Дата релиза', db_index=True)
    distributor = models.CharField(max_length=256, verbose_name='Название дистрибьютора', null=True)

class SourceUsers(models.Model):
    source_id = models.CharField(max_length=256, verbose_name='ID источника', db_index=True)
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', on_delete = models.PROTECT)
    profile = models.ForeignKey(Profile, verbose_name='Профиль', on_delete = models.PROTECT)


class Torrents(models.Model):
    film = models.IntegerField(verbose_name='KID фильма', db_index=True)
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', null=True, on_delete = models.PROTECT)
    go_link_id = models.CharField(max_length=32, verbose_name='ID ссылки', null=True)
    link = models.CharField(max_length=256, verbose_name='Ссылка на трекер', null=True)
    tracker = models.CharField(max_length=64, verbose_name='Трекер', null=True)
    quality = models.CharField(max_length=32, verbose_name='Качество', null=True) # DVDRip, CamRip ...
    quality_avg = models.CharField(max_length=1, choices=TORRENT_QUALITY, verbose_name='Качество', null=True) # хорошее, плохое ...
    file_size = models.CharField(max_length=32, verbose_name='Размер файла', null=True)
    path = models.CharField(max_length=256, verbose_name='Торрент файл', null=True)

class TorrentsUsers(models.Model):
    torrent = models.ForeignKey(Torrents, verbose_name='Торрент', on_delete = models.PROTECT)
    profile = models.ForeignKey(Profile, verbose_name='Профиль', null=True, on_delete=models.SET_NULL)
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата время получения')
    got = models.BooleanField(verbose_name='Был ли файл скачан', default=False)

class FestCompetition(models.Model):
    name_en = models.CharField(max_length=256, verbose_name='Англ. название')
    name_ru = models.CharField(max_length=256, verbose_name='Русс. название')
    type = models.CharField(max_length=1, choices=FEST_TYPE_CHOICES, verbose_name='Тип')

class AwardsNames(models.Model):
    name_en = models.CharField(max_length=256, verbose_name='Англ. название', blank=True, null=True)
    name_ru = models.CharField(max_length=256, verbose_name='Русс. название', blank=True, null=True)

class Awards(models.Model):
    awards = models.ForeignKey(AwardsNames, verbose_name='Название награды/номинации', on_delete = models.PROTECT)
    year = models.IntegerField(verbose_name='Год', null=True)
    type = models.CharField(max_length=1, choices=AWARDS_CHOICES, verbose_name='Тип')
    fest = models.ForeignKey(FestCompetition, verbose_name='Фестиваль', on_delete = models.PROTECT)

class AwardsRelations(models.Model):
    kid = models.IntegerField(verbose_name='KID фильма')
    awards = models.ManyToManyField(Awards, verbose_name='Награда', null=True)



class Top250(models.Model):
    key = models.CharField(max_length=256, verbose_name='Уникальный ключ')
    date_upd = models.DateField(verbose_name='Дата обновления')
    film = models.ForeignKey(SourceFilms, verbose_name='Фильм', on_delete = models.PROTECT)
    position = models.IntegerField(verbose_name='Позиция в рейтинге')
    change = models.IntegerField(verbose_name='Изменение позиции') #1-нет, 2-вверх, 3-вниз, 4-новый
    change_val = models.IntegerField(verbose_name='На сколько позиций', null=True)
    rating = models.FloatField(verbose_name='Рейтинг')
    votes = models.IntegerField(verbose_name='Кол-во голосов')
    class Meta:
        ordering = ['date_upd']



class Okinoua(models.Model):
    imdb = models.IntegerField(verbose_name='ID IMDB фильма', blank=True, null=True)
    kid = models.IntegerField(verbose_name='KID фильма')
    url = models.URLField(max_length=256, verbose_name='url')
    name_ru = models.CharField(max_length=128, verbose_name='Русское название фильма')
    name_ua = models.CharField(max_length=128, verbose_name='Украинское название фильма', blank=True, null=True)
    release = models.DateField(verbose_name='Дата релиза')
    distributor = models.CharField(max_length=256, verbose_name='Название дистрибьютора')


class RaspishiRelations(models.Model):
    rid = models.IntegerField(verbose_name='ID источника')
    kid = models.IntegerField(verbose_name='KID фильма', blank=True, null=True, db_index=True)
    name_ru = models.CharField(max_length=128, verbose_name='Русское название фильма')
    name_en = models.CharField(max_length=128, verbose_name='Англ. название фильма', blank=True, null=True)


class StatisticsDetails(models.Model):
    source = models.IntegerField(verbose_name='ID источника')
    cinemas = models.IntegerField(verbose_name='Всего кинотеатров у источника')
    cinemas_sale = models.IntegerField(verbose_name='Всего кинотеатров у источника с продажей')
    films = models.IntegerField(verbose_name='Всего фильмов у источника')
    sessions = models.IntegerField(verbose_name='Всего сеансов у источника')
    sessions_sale = models.IntegerField(verbose_name='Всего сеансов у источника с продажей')


class Statistics(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    sessions = models.IntegerField(verbose_name='Всего сеаснов')
    sessions_sale = models.IntegerField(verbose_name='Сеансов с продажей')
    cinemas = models.IntegerField(verbose_name='Всего кинотеатров')
    cinemas_sale = models.IntegerField(verbose_name='Кинотеатров с продажей')
    films = models.IntegerField(verbose_name='Всего фильмов')
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата время статистики', editable=False)
    details = models.ManyToManyField(StatisticsDetails, verbose_name='Статистика по источникам', blank=True, null=True)


class Nowru(models.Model):
    nowru_id = models.IntegerField(verbose_name='ID now.ru')
    idec = models.IntegerField(verbose_name='idec')
    kinopoisk_id = models.IntegerField(verbose_name='ID кинопоиск', blank=True, null=True)
    kid = models.IntegerField(verbose_name='KID', blank=True, null=True, db_index=True)
    regions = models.CharField(max_length=256, verbose_name='Регионы')
    name_ru = models.CharField(max_length=128, verbose_name='Русское название фильма')
    name_en = models.CharField(max_length=128, verbose_name='Нерусское название фильма', blank=True, null=True)
    year = models.IntegerField(verbose_name='Год', blank=True, null=True)
    player_code = models.CharField(max_length=256, verbose_name='Код плеера')
    url_api = models.URLField(max_length=256, verbose_name='url api')
    url_web = models.URLField(max_length=256, verbose_name='url web')
    url_poster = models.URLField(max_length=256, verbose_name='url постера', blank=True, null=True)
    url_image = models.URLField(max_length=256, verbose_name='url изображения', blank=True, null=True)
    url_player = models.URLField(max_length=256, verbose_name='url показа онлайн', blank=True, null=True)
    rel_ignore = models.BooleanField(verbose_name='Игнориовать', default=False)

class UkrainePosters(models.Model):
    source_id = models.CharField(max_length=128, verbose_name='ID источника')
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', on_delete = models.PROTECT)
    poster = models.CharField(max_length=100, verbose_name='Путь к постеру', blank=True)
    kid = models.IntegerField(verbose_name='KID фильма')


class Releases(models.Model):
    '''
    Релизы
    '''
    name_ru = models.CharField(max_length=128, verbose_name='Русское название фильма')
    name_en = models.CharField(max_length=128, verbose_name='Нерусское название фильма')
    details = models.CharField(max_length=128, verbose_name='Детали', blank=True, null=True)
    film_id = models.IntegerField(verbose_name='ID фильма на источнике', db_index=True)
    url = models.URLField(max_length=256, verbose_name='url')
    release_date = models.DateField(verbose_name='Дата релиза', db_index=True)
    distributor1 = models.CharField(max_length=128, verbose_name='Дистрибьютор1', blank=True, null=True)
    distributor1_id = models.CharField(max_length=24, verbose_name='ID дистрибьютора1', blank=True, null=True)
    distributor2 = models.CharField(max_length=128, verbose_name='Дистрибьютор2', blank=True, null=True)
    distributor2_id = models.CharField(max_length=24, verbose_name='ID дистрибьютора2', blank=True, null=True)
    copies = models.IntegerField(verbose_name='Число копий', blank=True, null=True)
    runtime = models.IntegerField(verbose_name='Хронометраж', blank=True, null=True)
    class Meta:
        verbose_name = u'Релиз'
        verbose_name_plural = u'Релизы'


class ReleasesRelations(models.Model):
    '''
    Связь релизов с киноафишей
    '''
    film_kid = models.IntegerField(verbose_name='KID фильма', db_index=True)
    distributor_kid = models.IntegerField(verbose_name='KID дистрибьютора')
    release = models.ForeignKey(Releases, verbose_name='Релиз', on_delete = models.PROTECT)
    rel_profile = models.ForeignKey(Profile, verbose_name='Кто связал', null=True, on_delete = models.PROTECT)
    rel_dtime = models.DateTimeField(verbose_name='Когда связал', null=True)
    rel_double = models.BooleanField(verbose_name='Дубль', default=False)
    rel_ignore = models.BooleanField(verbose_name='Игнориовать', default=False)

class NotFoundFilmsRelations(models.Model):
    '''
    Связь ненайденных фильмов с киноафишей
    '''
    name = models.CharField(max_length=128, verbose_name='Название slug')
    kid = models.IntegerField(verbose_name='KID фильма')
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', null=True, on_delete = models.PROTECT)


class NotFoundCinemasRelations(models.Model):
    '''
    Связь ненайденных кинотеатров с киноафишей
    '''
    name = models.CharField(max_length=128, verbose_name='Название slug')
    kid = models.IntegerField(verbose_name='KID кинотеатра')
    city = models.ForeignKey(City, verbose_name='Город', null=True, on_delete = models.PROTECT)


class NotFoundPersonsRelations(models.Model):
    '''
    Связь ненайденных персон с киноафишей
    '''
    name = models.CharField(max_length=128, verbose_name='Название slug')
    kid = models.IntegerField(verbose_name='KID персоны')


class SubscriptionRelease(models.Model):
    '''
    Связь пользователя с релизом
    '''
    profile = models.ForeignKey(Profile, verbose_name='Профиль пользователя', on_delete = models.PROTECT)
    release = models.ForeignKey(ReleasesRelations, verbose_name='Релиз', null=True, on_delete = models.PROTECT)
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата время подписки', blank=True, null=True)
    notified = models.BooleanField(verbose_name='Уведомлен ли', default=False)
    kid = models.IntegerField(verbose_name='KID фильма', null=True, db_index=True)

class SubscriptionTopics(models.Model):
    '''
    Подписка на фильм в сети
    '''
    profile = models.ForeignKey(Profile, verbose_name='Профиль пользователя', on_delete = models.PROTECT)
    kid = models.IntegerField(verbose_name='KID фильма')
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата время подписки', blank=True, null=True)
    notified = models.BooleanField(verbose_name='Уведомлен ли', default=False)
    quality = models.CharField(max_length=1, choices=TORRENT_QUALITY, verbose_name='Качество', null=True)

class SessionsAfishaRelations(models.Model):
    kid = models.IntegerField(verbose_name='KID сеанса', db_index=True)
    source = models.ForeignKey(ImportSources, verbose_name='Источник', on_delete = models.PROTECT)
    schedule = models.ForeignKey(SourceSchedules, verbose_name='Сеанс источника', on_delete = models.PROTECT)


class BoxOffice(models.Model):
    bx_id = models.CharField(max_length=256, verbose_name='ID данных о сборах для фильма')
    source_id = models.CharField(max_length=256, verbose_name='ID фильма на источнике')
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Название фильма у источника')
    kid = models.IntegerField(verbose_name='KID фильма', db_index=True)
    distributor = models.ManyToManyField(Distributors, verbose_name='Дистрибьютор', related_name='box_office')
    screens = models.IntegerField(verbose_name='Кол-во экранов', null=True)
    date_from = models.DateField(verbose_name='Дата начала', null=True)
    date_to = models.DateField(verbose_name='Дата окончания', null=True)
    week_sum = models.IntegerField(verbose_name='Сборы за неделю', null=True)
    all_sum = models.IntegerField(verbose_name='Сборы за весь период', null=True)
    week_audience = models.IntegerField(verbose_name='Зрителей за неделю', null=True)
    all_audience  = models.IntegerField(verbose_name='Зрителей за весь период', null=True)
    days = models.IntegerField(verbose_name='Дней в прокате', null=True)
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete = models.PROTECT)


class CurrencyRate(models.Model):
    '''
    Курс валюты. 1 USD к другой валюте
    '''
    currency = models.CharField(max_length=1, choices=CURRENCY_CHOICES, verbose_name='Валюта')
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete = models.PROTECT)
    value = models.FloatField(verbose_name='Значение')
    by_currency = models.CharField(max_length=1, choices=CURRENCY_CHOICES, verbose_name='За 1 еденицу валюты')
    date = models.DateField(verbose_name='Дата курса')

class SubscriptionFeeds(models.Model):
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата время подписки')
    profile = models.ForeignKey(Profile, verbose_name='Профиль пользователя', on_delete = models.PROTECT)
    type = models.CharField(max_length=1, choices=RSS_FEEDS_CHOICES, verbose_name='На что подписан')


class BuyTicketStatistic(models.Model):
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата время')
    profile = models.ForeignKey(Profile, verbose_name='Профиль пользователя', on_delete = models.PROTECT)
    session = models.ForeignKey(SourceSchedules, verbose_name='Сеанс', on_delete = models.PROTECT)
    country = models.ForeignKey(Country, verbose_name='Страна', null=True, on_delete = models.PROTECT)



class ProjectStages(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название этапа')
    start_date = models.DateField(verbose_name='Дата старта')
    end_date = models.DateField(verbose_name='Дата релиза')
    budget = models.IntegerField(verbose_name='Бюджет')

    def __unicode__(self):
       return '%s' % self.name


class Projects(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название проекта')
    url = models.CharField(max_length=128, verbose_name='URL', null=True)
    start_date = models.DateField(verbose_name='Дата старта', null=True)
    release_date = models.DateField(verbose_name='Дата релиза', null=True)
    director = models.ForeignKey(Profile, null=True, on_delete = models.PROTECT)
    directors = models.ManyToManyField(Profile, related_name="project_directors")
    members = models.ManyToManyField(Profile, related_name="project_members")
    sms = models.BooleanField(verbose_name='Notify by SMS', default=False)
    email = models.BooleanField(verbose_name='Notify by E-mail', default=True)
    budget = models.IntegerField(verbose_name='Бюджет', null=True)
    currency = models.CharField(max_length=1, choices=CURRENCY_CHOICES, verbose_name='Валюта', null=True)
    is_public = models.BooleanField(verbose_name='Показывать всем', default=True)
    stages = models.ManyToManyField(ProjectStages, verbose_name='Этапы')

    def __unicode__(self):
       return '%s' % self.name

class ActionsPriceList(models.Model):
    title = models.CharField(max_length=128, verbose_name='Действие')
    price = models.FloatField(verbose_name='Цена')
    price_edit = models.FloatField(verbose_name='Цена редактирования', null=True)
    price_delete = models.FloatField(verbose_name='Цена удаления', null=True)
    allow = models.BooleanField(verbose_name='Учитывать', default=False)
    group = models.CharField(max_length=2, choices=ACTION_OBJ_CHOICES, verbose_name='Группа дейсвий', default='0')
    #project = models.CharField(max_length=1, choices=JOB_PROJECTS_NAMES, verbose_name='Проект', default='1')
    user_group = models.ForeignKey(Group, null=True, verbose_name='Группа пользователей', on_delete = models.PROTECT)
    project = models.ForeignKey(Projects, verbose_name='Проект', default='1', on_delete = models.PROTECT)

class PaidActions(models.Model):
    profile = models.ForeignKey(Profile, verbose_name='Профиль пользователя', on_delete = models.PROTECT)
    action = models.ForeignKey(ActionsPriceList, verbose_name='Оплачиваемое действие', on_delete = models.PROTECT)
    object = models.CharField(max_length=256, verbose_name='Объект над которым произошло действие', null=True)
    extra = models.CharField(max_length=256, verbose_name='Дополнительные сведения', null=True)
    text = models.TextField(verbose_name='Описание', blank=True, null=True)
    dtime = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    allow = models.BooleanField(verbose_name='Учитывать', default=False)
    ignore = models.BooleanField(verbose_name='Не оплачивать', default=False)
    number = models.IntegerField(verbose_name='Кол-во действий', default=1)
    act = models.CharField(max_length=1, choices=ACTION_CHOICES, verbose_name='Действие', null=True)
    stage = models.ForeignKey(ProjectStages, verbose_name='Этап работы', null=True, on_delete = models.PROTECT)

    future = models.BooleanField(verbose_name='Задание на будущее', default=False)
    director = models.ForeignKey(Profile, related_name="director_%(class)s", null=True, verbose_name='Профиль директора', on_delete = models.PROTECT)
    is_accepted = models.BooleanField(verbose_name='Принято в работу (админом)', default=False)


class ActionsLog(models.Model):
    dtime = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    profile = models.ForeignKey(Profile, verbose_name='Профиль пользователя', on_delete = models.PROTECT)
    object = models.CharField(max_length=2, choices=ACTION_OBJ_CHOICES, verbose_name='Объект')
    object_id = models.IntegerField(verbose_name='ID объекта')
    action = models.CharField(max_length=1, choices=ACTION_CHOICES, verbose_name='Действие')
    attributes = models.CharField(max_length=256, verbose_name='Измененные свойства объекта', null=True)
    site = models.ForeignKey(DjangoSite, editable=False, verbose_name='Сайт', default=1, on_delete = models.PROTECT)


class NewsTags(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название метки, тега')


class News(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    dtime = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    visible = models.BooleanField(verbose_name='Показывать ли', default=False)
    img = models.CharField(max_length=256, verbose_name='Изображение', null=True)
    video = models.CharField(max_length=256, verbose_name='Видео', null=True, blank=True)
    tags = models.ManyToManyField(NewsTags, verbose_name='Метки', null=True)
    autor = models.ForeignKey(Profile, verbose_name='Автор', editable=False, null=True, on_delete = models.PROTECT)
    site = models.ForeignKey(DjangoSite, editable=False, verbose_name='Сайт', on_delete = models.PROTECT)
    subdomain = models.CharField(max_length=128, editable=False, verbose_name='Субдомен')
    world_pub = models.BooleanField(verbose_name='Публиковать на всех сайтах', default=False)
    reader_type = models.CharField(max_length=2, choices=NEWS_CHOICES, verbose_name='Тип сообщения', null=True)
    autor_status = models.BooleanField(verbose_name='Видно автору', default=True)
    autor_nick = models.IntegerField(verbose_name='Подпись', default=0) # 0 - обычная, 1 - псевдоним, 2 - скрыта
    extra = models.CharField(max_length=256, verbose_name='Доп.поле', null=True)
    kid = models.IntegerField(verbose_name='Импорт из киноафиши', null=True, db_index=True)
    language = models.ForeignKey(Language, null=True, on_delete = models.PROTECT)
    translation_for = models.ForeignKey('self', null=True, related_name='translate_for_rel', on_delete = models.PROTECT)
    views = models.IntegerField(verbose_name='Просмотров', default=0)
    parent = models.ForeignKey('self', null=True, related_name='parent_rel', on_delete = models.PROTECT)
    branch = models.ForeignKey('self', null=True, related_name='branch_rel', on_delete = models.PROTECT)

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
        ordering: ['-id']
    def __unicode__(self):
        return '%s' % (self.title)


class NewsAlterTranslation(models.Model):
    news = models.ForeignKey(News, on_delete = models.PROTECT)
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    tags = models.ManyToManyField(NewsTags, verbose_name='Метки', null=True)
    language = models.ForeignKey(Language, on_delete = models.PROTECT)


class NewsFilms(models.Model):
    kid = models.IntegerField(verbose_name='KID фильма', db_index=True)
    message = models.ForeignKey(News, verbose_name='Сообщение', on_delete = models.PROTECT)
    source_id = models.CharField(max_length=128, verbose_name='ID источника', null=True)
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', editable=False, null=True, on_delete = models.PROTECT)
    rate = models.IntegerField(verbose_name='Оценка', null=True) # интегральная оценка от 2 до 5
    rate_1 = models.IntegerField(null=True) # оценка от 3 до 9 eye
    rate_2 = models.IntegerField(null=True) # оценка от 3 до 9 mind
    rate_3 = models.IntegerField(null=True) # оценка от 3 до 9 heart

class NewsReaders(models.Model):
    user = models.ForeignKey(Profile, verbose_name='Связь с юзером', on_delete = models.PROTECT)
    status = models.CharField(max_length=1, choices=MESSENGER_CHOICES, verbose_name='Тип действия с сообщением')
    message = models.ForeignKey(News, verbose_name='Сообщение', on_delete = models.PROTECT)

class DialogMessages(models.Model):
    readers = models.ManyToManyField(NewsReaders, verbose_name='Пользователь адресат')
    #messages = models.ManyToManyField(News)



class OrganizationPhones(models.Model):
    phone = models.CharField(max_length=64, verbose_name='Номер телефона')
    note = models.CharField(max_length=128, verbose_name='Примечание', null=True)


class OrganizationImages(models.Model):
    img = models.CharField(max_length=256, verbose_name='Изображение')
    status = models.IntegerField(verbose_name='Статус 1 - главное, 2 - альт.')


class OrganizationTags(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название метки, тега')
    alter_name = models.CharField(max_length=128, verbose_name='Альтернативное название метки, тега', null=True)
    group_flag = models.CharField(max_length=1, choices=TAG_GROUP_CHOICES, verbose_name='Групповая принадлежность', null=True)
    #group_flag = models.CharField(max_length=128, verbose_name='Групповая принадлежность:org_name_tag название;org_about_tag О_нас;org_offers_tag Предложение;org_needs_tag Спрос', null=True)

class OrganizationRelations(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    link = models.CharField(max_length=256, verbose_name='Ссылка')

class OrganizationMenu(models.Model):
    tag = models.ForeignKey(OrganizationTags, verbose_name='Метка', on_delete = models.PROTECT)

class Organization(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    uni_slug = models.CharField(max_length=256, verbose_name='Название латиницей, очищенное', db_index=True)
    slug = models.CharField(max_length=256, verbose_name='очищенное')
    ownership = models.CharField(max_length=1, choices=OWNERSHIP_CHOICES, verbose_name='Форма собс.', null=True)
    buildings = models.ManyToManyField(Building, verbose_name='Здание', null=True)
    room_num = models.IntegerField(verbose_name='Номер', null=True)
    room_type = models.CharField(max_length=1, choices=ROOM_TYPE_CHOICES, verbose_name='Помещение', null=True)
    phones = models.ManyToManyField(OrganizationPhones, verbose_name='Телефоны', null=True)
    site = models.URLField(null=True, verbose_name='Сайт', blank=True)
    email = models.CharField(max_length=256, verbose_name='E-mail', null=True, blank=True)
    note = models.TextField(verbose_name='Заметка', null=True, blank=True)
    note_accept = models.BooleanField(verbose_name='Проверена модератором', default=True)
    source_obj = models.ForeignKey(ImportSources, verbose_name='Источник', editable=False, null=True, on_delete = models.PROTECT)
    source_id = models.CharField(max_length=256, verbose_name='ID источника', editable=False, null=True)
    tags = models.ManyToManyField(OrganizationTags, through='Organization_Tags', verbose_name='Метки')
    #edited = models.DateTimeField(verbose_name='Дата время редактирования', null=True, editable=False)
    #profile = models.ForeignKey(Profile, verbose_name='Профиль редактора', null=True)
    trailer = models.CharField(max_length=256, verbose_name='Трейлер', null=True, blank=True)
    images = models.ManyToManyField(OrganizationImages, verbose_name='Изображения', null=True)
    creator = models.ForeignKey(Profile, verbose_name='Автор', editable=False, null=True, on_delete = models.PROTECT)
    rate = models.IntegerField(verbose_name='Репутация', null=True)
    visible = models.BooleanField(verbose_name='Показывать ли', default=True)
    owner = models.CharField(max_length=128, verbose_name='Владелец, будет ссылкой на профиль я-всети', null=True)
    alter_name = models.CharField(max_length=256, verbose_name='Временное поле для хранения спарсенных данных из name', null=True)
    editors = models.ManyToManyField(Profile, verbose_name='Редакторы', related_name="editors_%(class)s", null=True)
    staff = models.ManyToManyField(Profile, verbose_name='Сотрудники', related_name="staff_%(class)s", null=True)
    relations = models.ManyToManyField(OrganizationRelations, verbose_name='Связи', null=True)
    news = models.ManyToManyField(News, through='OrganizationNews', verbose_name='Новости - спрос, предложения, объявления')
    branding = models.CharField(max_length=256, verbose_name='Фон', null=True)
    domain = models.ForeignKey(DjangoSite, editable=False, null=True, on_delete = models.PROTECT)
    extra = models.CharField(max_length=256, verbose_name='Доп.данные', null=True, blank=True)
    kid = models.IntegerField(verbose_name='ID орг на киноафише', null=True, db_index=True)
    circuit = models.ForeignKey(CinemaCircuit, null=True, on_delete = models.PROTECT)

    class Meta:
        verbose_name = u'Организация'
        verbose_name_plural = u'Организации'
    def __unicode__(self):
        return '%s' % (self.name)


class OrganizationLang(models.Model):
    organization = models.ForeignKey(Organization, on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Название', blank=True)
    note = models.TextField(verbose_name='Заметка', null=True, blank=True)
    buildings = models.ManyToManyField(Building, verbose_name='Здание', null=True)
    extra = models.CharField(max_length=256, verbose_name='Доп.данные', null=True, blank=True)
    language = models.ForeignKey(Language, on_delete = models.PROTECT)


class Organization_Tags(models.Model):
    organizationtags = models.ForeignKey(OrganizationTags, on_delete = models.PROTECT)
    organization = models.ForeignKey(Organization, on_delete = models.PROTECT)


class OrganizationNews(models.Model):
    news = models.ForeignKey(News, on_delete = models.PROTECT)
    organization = models.ForeignKey(Organization, on_delete = models.PROTECT)
    tag = models.ForeignKey(Organization_Tags, null=True, on_delete = models.PROTECT)
    #group_flag = models.CharField(max_length=1, choices=TAG_GROUP_CHOICES, verbose_name='Групповая принадлежность')

class AfishaCinemaRate(models.Model):
    rate1 = models.IntegerField()
    rate2 = models.IntegerField()
    rate3 = models.IntegerField()
    rate = models.FloatField()
    vnum = models.IntegerField()
    organization = models.ForeignKey(Organization, on_delete = models.PROTECT)


class ProjectsGallery(models.Model):
    photo = models.ForeignKey(Images, on_delete = models.PROTECT)
    title = models.CharField(max_length=128, verbose_name='Название', blank=True, null=True)
    description = models.TextField(verbose_name='Примечание', blank=True, null=True)

class ProjectsGalleryLang(models.Model):
    gallery = models.ForeignKey(ProjectsGallery, on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Название')
    title = models.CharField(max_length=128, verbose_name='Название', blank=True, null=True)
    description = models.TextField(verbose_name='Примечание', blank=True, null=True)
    language = models.ForeignKey(Language, on_delete = models.PROTECT)


class OrgSubMenu(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    news = models.ManyToManyField(News)
    gallery = models.ManyToManyField(ProjectsGallery)
    page_type = models.CharField(max_length=1, choices=PAGE_TYPES_CHOICES, verbose_name='Тип страницы', default='0', null=True)
    url = models.CharField(max_length=64, verbose_name='URL', null=True)
    booker_profile = models.ForeignKey(Profile, verbose_name='Связь с букером', null=True, on_delete = models.PROTECT)


class OrgSubMenuLang(models.Model):
    orgsubmenu = models.ForeignKey(OrgSubMenu, on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Название')
    language = models.ForeignKey(Language, on_delete = models.PROTECT)


class OrgMenu(models.Model):
    organization = models.ForeignKey(Organization, verbose_name='Организация', null=True, on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Название')
    submenu = models.ManyToManyField(OrgSubMenu, verbose_name='Подменю')
    profile = models.ForeignKey(Profile, verbose_name='Профиль', null=True, on_delete = models.PROTECT)
    private = models.BooleanField(verbose_name='Только для владельца', default=False)

class OrgMenuLang(models.Model):
    orgmenu = models.ForeignKey(OrgMenu, on_delete = models.PROTECT)
    name = models.CharField(max_length=256, verbose_name='Название')
    language = models.ForeignKey(Language, on_delete = models.PROTECT)


class EmailNotice(models.Model):
    '''
    Защита от дураков.
    Ограничение уведомлений для юзера за определенный промежуток времени.
    Например, юзер может отправить только 5 email сообщений (авторизация, приглашения) за 10 минут.
    '''
    email = models.CharField(max_length=256, verbose_name='e-mail')
    count = models.IntegerField(verbose_name='Кол-во сообщений', default=0)
    dtime = models.DateTimeField(verbose_name='Время отправления', auto_now_add=True, editable=False)
    type = models.IntegerField(verbose_name='Тип сообщения') # 1 - приглашение орг, 2 - авторизация


class MovieMegogo(models.Model):
    '''
    Модель для парсинга с мегого
    '''
    afisha_id = models.IntegerField(null=True, db_index=True)  # идентификация айди киноафиши
    megogo_id = models.IntegerField(null=True)  # ид фильма мегого используется в плеере
    title = models.CharField(max_length=128, null=True)  # название
    title_en = models.CharField(max_length=128, null=True)  # название en
    genres = models.CharField(max_length=256, null=True)  # жанры
    serial = models.BooleanField()  # сериал (true/false)
    page = models.CharField(max_length=256, null=True)  # страница фильма на мегого
    type_f = models.CharField(max_length=10, null=True)  # тип (фильм, мультфильм, новсть)
    kinopoisk_id = models.IntegerField(null=True)  # id на кинопоске
    year = models.IntegerField(null=True) # год производства
    country = models.CharField(max_length=128, null=True)  # страна производитель
    budget = models.CharField(max_length=20, null=True)  # бюджет фильма
    premiere = models.CharField(max_length=20, null=True) # дата примеры
    dvd = models.CharField(max_length=20, null=True) # дата выхода на dvd
    duration = models.CharField(max_length=20, null=True)  # длительность
    kinopoisk = models.FloatField(null=True) # рейтинг на кинопоиске
    imdb = models.FloatField(null=True) # рейтинг на imdb
    story = models.TextField(null=True)  # описание фильма
    poster_url = models.CharField(max_length=256, null=True)  # адрес постер 126px × 71px
    poster_thumbnail = models.CharField(max_length=256, null=True)  # адрес постера 720px × 400px
    rel_ignore = models.BooleanField(verbose_name='Игнориовать', default=False)

class IntegralRating(models.Model):
    '''
    Модель для хранения интегральной оценки фильма:
    '''
    afisha_id = models.IntegerField(null=True, db_index=True)  # ид фильма в базе киноафиши
    i_rate  = models.FloatField(null=True)    # интегральная оценка
    trouble = models.CharField(max_length=50, null=True)   # причина отсутствия оценки
    imdb = models.FloatField(null=True)
    reviews = models.FloatField(null=True)
    rotten = models.FloatField(null=True)

class Background(models.Model):
    '''
    Фоновые баннеры
    '''
    image = models.ImageField(upload_to='bg')
    url = models.URLField(max_length=256, verbose_name="Сайт рекламодателя")
    country = models.ForeignKey(Country, verbose_name='Таргетинг на страну', on_delete = models.PROTECT)
    city = models.ForeignKey(City, verbose_name='Таргетинг на город', blank=True, null=True, on_delete = models.PROTECT)
    date_adding = models.DateTimeField(auto_now_add=True, editable=False)
    site = models.ForeignKey(DjangoSite, editable=False, on_delete = models.PROTECT)
    subdomain = models.CharField(max_length=128, editable=False, verbose_name='Субдомен', null=True)


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='Заголовок', blank=True, null=True)
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    dtime = models.DateTimeField(auto_now_add=True, editable=False)
    visible = models.BooleanField(verbose_name='Visible', default=False)
    def __unicode__(self):
        return '%s' % (self.title)
'''
class Invoices(models.Model):
    code = models.CharField(max_length=128)
    number = models.CharField(max_length=64)
    event = models.ForeignKey(DjangoSite, null=True)
    note =
    pdf = models.CharField(max_length=64, null=True)
    paid = models.BooleanField(default=False)
'''

class LetsGetClients(models.Model):
    profile = models.ForeignKey(Profile, null=True, on_delete = models.PROTECT)
    site = models.ForeignKey(DjangoSite, null=True, on_delete = models.PROTECT)
    subdomain = models.CharField(max_length=128, null=True)
    organization = models.ForeignKey(Organization, null=True, on_delete = models.PROTECT)
    tag = models.CharField(max_length=128, blank=True, null=True)
    #tags = models.ManyToManyField(OrganizationTags, verbose_name='Метки')

class LetsGetBank(models.Model):
    name = models.CharField(max_length=128)
    account = models.CharField(max_length=64)
    site = models.ForeignKey(DjangoSite, null=True, on_delete = models.PROTECT)
    subdomain = models.CharField(max_length=128, null=True)

class LetsGetCalendar(models.Model):
    event_name = models.CharField(max_length=256, verbose_name='Event Name', blank=True, null=True)
    event_place = models.CharField(max_length=256, verbose_name='Event Place', null=True)
    dtime = models.DateTimeField(verbose_name='Event DateTime', db_index=True)
    sms = models.BooleanField(verbose_name='Notify Clients by SMS', default=False)
    email = models.BooleanField(verbose_name='Notify Clients by E-mail', default=False)
    start_notify_sms = models.CharField(max_length=2, choices=TIME_MSG_CHOICES, verbose_name='Start Notify SMS', default=4)
    start_notify_email = models.CharField(max_length=2, choices=TIME_MSG_CHOICES, verbose_name='Start Notify E-mail', default=4)
    start_notify_sms_dtime = models.DateTimeField(null=True)
    start_notify_email_dtime = models.DateTimeField(null=True)
    type = models.CharField(max_length=1, choices=LETSGET_EVENTS_TYPE, verbose_name='Type', default=1)
    price = models.CharField(max_length=16, verbose_name='Price', blank=True, null=True)
    site = models.ForeignKey(DjangoSite, null=True, on_delete = models.PROTECT)
    subdomain = models.CharField(max_length=128, null=True)
    client = models.ForeignKey(LetsGetClients, on_delete = models.PROTECT)
    bank = models.ForeignKey(LetsGetBank, default=1, on_delete = models.PROTECT)
    note = models.TextField(blank=True, null=True)
    pdf = models.CharField(max_length=64, null=True)
    paid = models.BooleanField(default=False)
    bcr = models.IntegerField(null=True)
    bcr_code = models.CharField(max_length=128, null=True)
    num_sessions = models.IntegerField(default=1)
    invoice_template = models.ForeignKey(News, null=True, on_delete = models.PROTECT)
    auto = models.BooleanField(default=True)
    report = models.ForeignKey(News, null=True, related_name="report_%(class)s", on_delete = models.PROTECT)
    report_send = models.BooleanField(default=False)

class LetsGetCalendarNotified(models.Model):
    event = models.ForeignKey(LetsGetCalendar, on_delete = models.PROTECT)
    profile = models.ForeignKey(Profile, null=True, on_delete = models.PROTECT)
    organization = models.ForeignKey(Organization, null=True, on_delete = models.PROTECT)
    sms_notified = models.BooleanField(default=False)
    sms_status = models.CharField(max_length=128, blank=True, null=True)
    sms_dtime = models.DateTimeField(null=True)
    sms_id = models.CharField(max_length=64, blank=True, null=True)
    email_notified = models.BooleanField(default=False)
    email_status = models.CharField(max_length=128, blank=True, null=True)
    email_dtime = models.DateTimeField(null=True)
    invite_notified = models.BooleanField(default=False)
    invite_status = models.CharField(max_length=128, blank=True, null=True)
    invite_dtime = models.DateTimeField(null=True)
    invoice_notified = models.BooleanField(default=False)
    invoice_status = models.CharField(max_length=128, blank=True, null=True)
    invoice_dtime = models.DateTimeField(null=True)

class LetsGetCalendarClientNotified(models.Model):
    client = models.ForeignKey(LetsGetClients, on_delete = models.PROTECT)
    invite_notified = models.BooleanField(default=False)
    invite_status = models.CharField(max_length=128, blank=True, null=True)
    invite_dtime = models.DateTimeField(null=True, auto_now_add=True)

'''
class LetsGetCalendarLikes(models.Model):
    profile = models.ForeignKey(Profile)
    event = models.ForeignKey(LetsGetCalendar)
    vote = models.BooleanField() # 0 - unlike, 1 - like
'''

class WithdrawMoney(models.Model):
    summa = models.FloatField(verbose_name='Сумма')
    who = models.ForeignKey(Profile, null=True, related_name="who_%(class)s", verbose_name='Кто списывает', on_delete = models.PROTECT)
    profile = models.ForeignKey(Profile, null=True, related_name="profile_%(class)s", verbose_name='У кого списывает', on_delete = models.PROTECT)
    dtime = models.DateTimeField(verbose_name='Когда списавает', auto_now_add=True, editable=False)


class UserDeposit(models.Model):
    summa = models.FloatField(verbose_name='Сумма')
    profile = models.ForeignKey(Profile, null=True, verbose_name='Для кого', on_delete = models.PROTECT)
    dtime = models.DateTimeField(verbose_name='Когда начислено', auto_now_add=True, editable=False)



class WomenForumIgnored(models.Model):
    type = models.IntegerField(verbose_name='Тип игнора')  # 1 - сообщение, 2 - все в теме, 3 - все на форуме
    msg = models.IntegerField(verbose_name='ID сообщения на форуме', null=True, db_index=True)
    branch = models.IntegerField(verbose_name='ID топика на форуме', null=True)
    author = models.IntegerField(verbose_name='ID автора на форуме', null=True)
    user = models.IntegerField(verbose_name='ID юзера на форуме')


class WomenForumIgnoreLevel(models.Model):
    '''
    Если юзер имеет type = 1, то может игнорировать сообщения по одному
    type = 2, то может игнорировать сообщения автора в теме
    type = 3, то может игнорировать сообщения автора по всему форуму
    '''
    user = models.IntegerField(verbose_name='ID юзера на форуме')
    dtime = models.DateTimeField(verbose_name='Дата и время перехода на уровень')
    type = models.IntegerField(verbose_name='Тип игнора', db_index=True) # 1 - сообщение, 2 - все в теме, 3 - все на форуме


class BannedUsersAndIPs(models.Model):
    profile = models.ForeignKey(Profile, null=True, related_name="profile_%(class)s", on_delete = models.PROTECT)
    ip = models.CharField(max_length=15, null=True, db_index=True)
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время блокировки')
    who = models.ForeignKey(Profile, related_name="who_%(class)s", verbose_name='Кто заблокировал', on_delete = models.PROTECT)


class WomenForumLikes(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.PROTECT)
    msg = models.IntegerField(verbose_name='ID сообщения на форуме', db_index=True)
    like_type = models.BooleanField() # 0 - dislike, 1 - like

class ForumGeneral(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название форума')
    topics = models.ManyToManyField(News, verbose_name='Топики')
    site = models.ForeignKey(DjangoSite, on_delete = models.PROTECT)


class Mediafiles(models.Model):
    sign = models.CharField(max_length=256, verbose_name='ID файла')
    path = models.CharField(max_length=256, verbose_name='Путь к файлу')
    profile = models.ForeignKey(Profile, verbose_name='Кто загрузил', on_delete = models.PROTECT)
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время загрузки')
    tmp = models.BooleanField(default=True, verbose_name='Статус временного файла')
    size = models.CharField(max_length=32, verbose_name='Размер', blank=True, null=True)
    bitrate = models.CharField(max_length=32, verbose_name='Битрейт', blank=True, null=True)
    runtime = models.CharField(max_length=16, verbose_name='Хронометраж', blank=True, null=True)
    original_file_name = models.CharField(max_length=256, verbose_name='Оригинальное название файла', blank=True, null=True)
    original_artist = models.CharField(max_length=128, verbose_name='Оригинальное название артиста', blank=True, null=True)
    original_album = models.CharField(max_length=128, verbose_name='Оригинальное название альбома', blank=True, null=True)
    original_title = models.CharField(max_length=128, verbose_name='Оригинальное название трека', blank=True, null=True)
    mtype = models.CharField(max_length=1, choices=MUSIC_TYPE, verbose_name='Тип', default='0')
    tags = models.ManyToManyField(NewsTags, verbose_name='Теги')


class CompositionName(models.Model):
    #1 - рус
    #2 - оригинал
    #3 - международное
    #4 - альтернатив
    #5 - очищенное
    status = models.IntegerField(verbose_name='Статус')
    name = models.CharField(max_length=256, verbose_name='Имя персоны')

    def __unicode__(self):
        return '%s' % (self.name)

class Composition(models.Model):
    name = models.ManyToManyField(CompositionName, verbose_name='Названия')
    runtime = models.CharField(max_length=16, verbose_name='Хронометраж', null=True)
    year = models.IntegerField(verbose_name='Год релиза', null=True)
    country = models.ManyToManyField(Country, verbose_name='Страны')
    person = models.ManyToManyField(Person, through='CompositionPersonRel', verbose_name='Персоны', related_name="key_person_%(class)s")
    tags = models.ManyToManyField(NewsTags, verbose_name='Теги')
    #assignment =
    notes = models.TextField(blank=True, null=True)
    tablature = models.TextField(blank=True, null=True)
    text = models.ManyToManyField(News, verbose_name='Тексты, транскрипции')
    source_id = models.CharField(max_length=256, verbose_name='ID источника', null=True)
    media = models.ManyToManyField(Mediafiles, verbose_name='Медиафайлы')


class CompositionTrackTmp(models.Model):
    url = models.CharField(max_length=256)
    error = models.BooleanField()


class CompositionPersonType(models.Model):
    name = models.CharField(max_length=64, verbose_name='Тип') #текст, музыка, аранжировка, исполнение

class CompositionPersonRel(models.Model):
    person = models.ForeignKey(Person, on_delete = models.PROTECT)
    type = models.ManyToManyField(CompositionPersonType)
    composition = models.ForeignKey(Composition, on_delete = models.PROTECT)


class SiteBanners(models.Model):
    sites = models.ManyToManyField(DjangoSite, verbose_name='Сайты - площадки')
    profile = models.ForeignKey(Profile, verbose_name='Профиль - площадка', null=True, on_delete = models.PROTECT)
    file = models.CharField(max_length=256, verbose_name='Файл')
    name = models.CharField(max_length=128, verbose_name='Название')
    url = models.CharField(max_length=256, verbose_name='Название', null=True, blank=True)
    text = models.TextField(verbose_name='Текст', null=True, blank=True)
    budget = models.IntegerField(verbose_name='Бюджет', default=0)
    balance = models.FloatField(verbose_name='Остаток', default=0)
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата, время создания', null=True)
    last_show = models.DateField(auto_now_add=True, verbose_name='Дата последнего показа')
    country = models.ForeignKey(Country, verbose_name='Страна', null=True, on_delete = models.PROTECT)
    city = models.ForeignKey(City, verbose_name='Город', null=True, related_name="city_%(class)s", on_delete = models.PROTECT)
    style = models.CharField(max_length=32, verbose_name='Стиль', null=True, blank=True)
    user = models.ForeignKey(Profile, verbose_name='Автор', null=True, related_name="user_%(class)s", on_delete = models.PROTECT)
    btype = models.CharField(max_length=1, choices=BANNER_TYPE, verbose_name='Тип')
    views = models.IntegerField(verbose_name='Кол-во просмотров', default=0)
    cities = models.ManyToManyField(City)
    bg_disable_dtime_to = models.DateTimeField(verbose_name='Дата время до которого действует отмена фона', null=True)
    spent = models.FloatField(verbose_name='Потрачено средств на блок', default=0)
    deleted = models.BooleanField(verbose_name='Удален', default=False, db_index=True)

class SiteBannersClicks(models.Model):
    banner = models.ForeignKey(SiteBanners, verbose_name='Баннер', null=True, on_delete = models.PROTECT)
    profile = models.ForeignKey(Profile, verbose_name='Профиль юзера', null=True, on_delete=models.SET_NULL)
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата, время клика')

class SiteBannersViews(models.Model):
    banner = models.ForeignKey(SiteBanners, verbose_name='Баннер', null=True, on_delete = models.PROTECT)
    profile = models.ForeignKey(Profile, verbose_name='Профиль юзера', null=True, on_delete=models.SET_NULL)
    dtime = models.DateField(auto_now_add=True, verbose_name='Дата, время просмотра')



class SubscriberUser(models.Model):
    type = models.CharField(max_length=2, choices=SUBSCRIBE_TYPE, verbose_name='Тип объекта')
    obj = models.IntegerField(verbose_name='ID объекта')
    profile = models.ForeignKey(Profile, verbose_name='Профиль подписчика', on_delete = models.PROTECT)
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата, время подписки')
    unsubscribe = models.CharField(max_length=64, verbose_name='Код для отписки')

class SubscriberObjects(models.Model):
    type = models.CharField(max_length=2, choices=SUBSCRIBE_TYPE, verbose_name='Тип объекта')
    obj = models.IntegerField(verbose_name='ID объекта')
    end_obj = models.IntegerField(verbose_name='ID конечного объекта')
    in_work = models.BooleanField(verbose_name='В работе', default=True)

class SubscriberLog(models.Model):
    user = models.ForeignKey(SubscriberUser, verbose_name='Подписчик', on_delete = models.PROTECT)
    obj = models.ForeignKey(SubscriberObjects, verbose_name='Объект', on_delete = models.PROTECT)
    notified = models.BooleanField(verbose_name='Оповещен ли', default=True)
    dtime = models.DateTimeField(auto_now_add=True, verbose_name='Дата, время оповещения')
    error = models.CharField(max_length=128, verbose_name='Описание ошибки', null=True, blank=True)

class QuestionAnswer(models.Model):
    item = models.ManyToManyField(News)

class QAnswers(models.Model):
    item = models.ManyToManyField(News)



class UkrainianReleases(models.Model):
    kid = models.IntegerField(verbose_name='KID фильма')
    release = models.DateField(verbose_name='Дата релиза')




class BookingSettings(models.Model):
    profile = models.ForeignKey(Profile, verbose_name='Букер', on_delete = models.PROTECT)
    cinemas = models.ManyToManyField(Cinema, through='BookerCinemas', verbose_name='Кинотеатры')

class BookerCinemas(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete = models.PROTECT)
    settings = models.ForeignKey(BookingSettings, on_delete = models.PROTECT)
    permission = models.CharField(max_length=1, choices=BOOKER_PERMISSION, verbose_name='Права')

class BookingSchedules(models.Model):
    unique = models.CharField(max_length=64, verbose_name='ID')
    hall = models.ForeignKey(Hall, verbose_name='Зал', on_delete = models.PROTECT)
    dtime = models.DateTimeField(verbose_name='Дата, время сеанса', db_index=True)
    temp = models.BooleanField(verbose_name='Временный', default=False)
    films = models.ManyToManyField(SourceFilms, verbose_name='Фильмы')
