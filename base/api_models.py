# -*- coding: utf-8 -*-
from django.db import models

'''
Модели из базы asteroid
'''

# Модель описывает внешние объекты (файлы изображений, звука, видео)
class Extres(models.Model):
    extresid = models.IntegerField(primary_key=True, db_column='ExtResID')
    mimetype = models.CharField(max_length=120, db_column='MimeType')
    filename = models.CharField(max_length=300, db_column='FileName')
    filepath = models.CharField(max_length=750, db_column='FilePath')
    content = models.TextField(db_column='Content')
    info = models.TextField(db_column='Info')
    class Meta:
        db_table = u'ExtRes'
        managed = False

# модель связывает описание внешних объектов с типами и значениями
class Objxres(models.Model):
    objxresid = models.AutoField(primary_key=True, db_column='ObjXResID')
    extresid = models.ForeignKey(Extres, db_column='ExtResID', null=True, blank=True, on_delete = models.PROTECT)
    objtypeid = models.IntegerField(db_column='ObjTypeID')
    objpkvalue = models.IntegerField(db_column='ObjPKValue')
    class Meta:
        db_table = u'ObjXRes'
        managed = False

# Страны с Киноафиши
class AfishaCountry(models.Model):
    name = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    class Meta:
        db_table = u'country'
        managed = False

# города с Киноафиши
class AfishaCity(models.Model):
    name = models.CharField(max_length=75, blank=True)
    name_en = models.CharField(max_length=150)
    country = models.ForeignKey(AfishaCountry, db_column='id_country', null=True, blank=True, on_delete = models.PROTECT)
    class Meta:
        db_table = u'city'
        managed = False

# организации
class Company(models.Model):
    name = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    class Meta:
        db_table = u'company'
        managed = False

# жанры с Киноафиши
class AfishaGenre(models.Model):
    name = models.CharField(max_length=60, blank=True)
    name_en = models.CharField(max_length=60)
    class Meta:
        db_table = u'genre'
        managed = False

# кинопрокатывающие сети
class Seti(models.Model):
    name = models.CharField(max_length=150, db_column='Name')
    class Meta:
        db_table = u'Seti'
        managed = False

# станции метро
class AfishaMetro(models.Model):
    name = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = u'metro'
        managed = False

# организации-кинодистрибьюторы
class Prokat(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=511)
    phone = models.CharField(max_length=63)
    url = models.CharField(max_length=127)
    mail = models.CharField(max_length=63)
    comment = models.TextField()
    country = models.ForeignKey(AfishaCountry, db_column='country_id', null=True, on_delete = models.PROTECT)
    class Meta:
        db_table = u'prokat'
        managed = False

# Фильмы (старая плохая модель Киноафиши)
class Film(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    name = models.CharField(max_length=300)
    original_title = models.CharField(max_length=300, blank=True)
    country = models.ForeignKey(AfishaCountry, db_column='country', related_name='country', null=True, on_delete = models.PROTECT)
    year = models.CharField(max_length=60, blank=True)
    company = models.ForeignKey(Company, db_column='company', on_delete = models.PROTECT)
    genre1 = models.ForeignKey(AfishaGenre, db_column='genre1', related_name='genre1', null=True, on_delete = models.PROTECT)
    genre2 = models.ForeignKey(AfishaGenre, db_column='genre2', related_name='genre2', null=True, on_delete = models.PROTECT)
    genre3 = models.ForeignKey(AfishaGenre, db_column='genre3', related_name='genre3', null=True, on_delete = models.PROTECT)
    site = models.CharField(max_length=300)
    director1 = models.IntegerField()
    director2 = models.IntegerField()
    director3 = models.IntegerField()
    imdb = models.CharField(max_length=60, blank=True)
    imdb_votes = models.IntegerField()
    actor1 = models.IntegerField(null=True, blank=True)
    actor2 = models.IntegerField(null=True, blank=True)
    actor3 = models.IntegerField(null=True, blank=True)
    actor4 = models.IntegerField(null=True, blank=True)
    actor5 = models.IntegerField(null=True, blank=True)
    actor6 = models.IntegerField(null=True, blank=True)
    runtime = models.CharField(max_length=150, blank=True)
    limits = models.CharField(max_length=150, blank=True)
    prokat1 = models.ForeignKey(Prokat, db_column='prokat1', related_name='prokat1', null=True, blank=True, on_delete = models.PROTECT)
    prokat2 = models.ForeignKey(Prokat, db_column='prokat2', related_name='prokat2', null=True, blank=True, on_delete = models.PROTECT)
    date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    country2 = models.ForeignKey(AfishaCountry, db_column='country2', related_name='country2', null=True, on_delete = models.PROTECT)
    trailers = models.TextField()
    idalldvd = models.IntegerField(null=True, db_column='IdAllDVD', blank=True)
    datelastupd = models.DateTimeField(db_column='DateLastUpd')
    class Meta:
        db_table = u'film'
        managed = False

# названия фильмов
class FilmsName(models.Model):
    film_id = models.ForeignKey(Film, db_column='film_id', on_delete = models.PROTECT)
    name = models.CharField(max_length=127)
    type = models.IntegerField()
    status = models.IntegerField()
    hide = models.CharField(max_length=6)
    slug = models.CharField(max_length=127)
    class Meta:
        db_table = u'films_name'
        managed = False

# внешние данные (оценки и мнения) для фильма
class FilmExtData(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    rate1 = models.IntegerField()
    rate2 = models.IntegerField()
    rate3 = models.IntegerField()
    rate = models.FloatField()
    vnum = models.IntegerField()
    opinions = models.CharField(max_length=2)
    class Meta:
        db_table = u'film_ext_data'
        managed = False

# тип озвучания фильма
class FilmSoundType(models.Model):
    sound_type = models.CharField(max_length=63)
    class Meta:
        db_table = u'films_sound_type'
        managed = False

# название звука внутри типа
class FilmSound(models.Model):
    film_id = models.ForeignKey(Film, db_column='film_id', on_delete = models.PROTECT)
    type_sound = models.ForeignKey(FilmSoundType, db_column='type_sound', on_delete = models.PROTECT)
    num = models.IntegerField()
    class Meta:
        db_table = u'films_sound'
        managed = False

# оценки фильма от посетителей сайта
class FilmVotes(models.Model):
    rate_1 = models.IntegerField()
    rate_2 = models.IntegerField()
    rate_3 = models.IntegerField()
    class Meta:
        db_table = u'films_votes'
        managed = False

# кинотеатры
class Movie(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    name = models.CharField(max_length=150)
    city = models.ForeignKey(AfishaCity, db_column='city', null=True, on_delete = models.PROTECT)
    idterr = models.ForeignKey(AfishaCountry, db_column='IdTerr', null=True, on_delete = models.PROTECT)
    ind = models.CharField(max_length=18)
    address = models.CharField(max_length=150)
    phones = models.TextField()
    fax = models.CharField(max_length=150)
    mail = models.CharField(max_length=240)
    director = models.CharField(max_length=150)
    kontakt1 = models.CharField(max_length=150)
    kontakt2 = models.CharField(max_length=150)
    metro = models.ForeignKey(AfishaMetro, db_column='metro', null=True, on_delete = models.PROTECT)
    path = models.TextField()
    site = models.CharField(max_length=600)
    techinfo = models.TextField()
    set_field = models.ForeignKey(Seti, db_column='set', null=True, on_delete = models.PROTECT)
    workingtime = models.TextField()
    comment = models.TextField()
    access = models.IntegerField()
    random = models.IntegerField(unique=True)
    tech_comment = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    class Meta:
        db_table = u'movie'
        managed = False

# внешние (связанные) данные для кинотеатра (оценки и мнения)
class MovieExtData(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    rate1 = models.IntegerField()
    rate2 = models.IntegerField()
    rate3 = models.IntegerField()
    rate = models.FloatField()
    vnum = models.IntegerField()
    opinions = models.TextField()
    class Meta:
        db_table = u'movie_ext_data'
        managed = False

# ???
class ImpLoad(models.Model):
    movie = models.ForeignKey(Movie, db_column='movie', on_delete = models.PROTECT)
    source = models.IntegerField()
    url = models.CharField(max_length=256)
    class Meta:
        db_table = u'imp_load'
        managed = False

# названия залов кинотеатров
class AfishaHall(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    name = models.CharField(max_length=60)
    class Meta:
        db_table = u'hall'
        managed = False


class AfishaHalls(models.Model):
    id_name = models.ForeignKey(AfishaHall, db_column='id_name', null=True, on_delete = models.PROTECT)
    places = models.IntegerField()
    format = models.IntegerField()
    movie = models.ForeignKey(Movie, db_column='movie', null=True, on_delete = models.PROTECT)
    class Meta:
        db_table = u'halls'
        managed = False

class AfishaPersons(models.Model):
    birth_year = models.IntegerField()
    birth_mounth = models.IntegerField()
    birth_day = models.IntegerField()
    male = models.IntegerField()
    national = models.IntegerField()
    country = models.ForeignKey(AfishaCountry, db_column='country', null=True, on_delete = models.PROTECT)
    imdb = models.IntegerField()
    class Meta:
        db_table = u'persons'
        managed = False

class AfishaPersonsName(models.Model):
    person_id = models.ForeignKey(AfishaPersons, db_column='person_id', on_delete = models.PROTECT)
    name = models.CharField(max_length=127)
    name_cross = models.CharField(max_length=63)
    flag = models.IntegerField()
    class Meta:
        db_table = u'persons_name'
        managed = False

class PersonsHide(models.Model):
    film = models.ForeignKey(Film, db_column='film', on_delete = models.PROTECT)
    name = models.CharField(max_length=128)
    type = models.IntegerField()
    imdb = models.IntegerField()
    class Meta:
        db_table = u'persons_hide'
        managed = False

class PersonsStatusAct(models.Model):
    status_act = models.CharField(max_length=31)
    class Meta:
        db_table = u'persons_status_act'
        managed = False

class PersonsTypeAct(models.Model):
    type_act = models.CharField(max_length=31)
    class Meta:
        db_table = u'persons_type_act'
        managed = False

class PersonsRelationFilms(models.Model):
    person_id = models.ForeignKey(AfishaPersons, db_column='person_id', on_delete = models.PROTECT)
    film_id = models.ForeignKey(Film, db_column='film_id', on_delete = models.PROTECT)
    type_act_id = models.ForeignKey(PersonsTypeAct, db_column='type_act_id', on_delete = models.PROTECT)
    status_act_id = models.ForeignKey(PersonsStatusAct, db_column='status_act_id', on_delete = models.PROTECT)
    class Meta:
        db_table = u'persons_relation_films'
        managed = False

class Pictures(models.Model):
    object_id = models.IntegerField()
    object_type = models.IntegerField()
    face_picture = models.CharField(max_length=150)
    photos = models.TextField()
    class Meta:
        db_table = u'pictures'
        managed = False

class RegisteredUsers(models.Model):
    firstname = models.CharField(max_length=150, blank=True, default='')
    lastname = models.CharField(max_length=150, blank=True, default='')
    email = models.CharField(max_length=300, blank=True, default='')
    password = models.CharField(max_length=90, default='000000000000')
    access_level = models.IntegerField(default=0)
    date_registration = models.DateField(auto_now_add=True)
    country = models.IntegerField(default=0)
    city = models.IntegerField(default=0)
    sex = models.CharField(max_length=3, blank=True, default='')
    date_of_birth = models.DateField(default='0000-00-00')
    profession = models.IntegerField(default=0)
    organization = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    salt = models.CharField(max_length=36, default='000000000000')
    nickname = models.CharField(max_length=90)
    pass_text = models.CharField(max_length=765, default='!1#1!2#1!3#январь')
    movie = models.IntegerField(default=0)
    other = models.CharField(max_length=189, blank=True, default='')
    type_org = models.IntegerField(default=0)
    type_m = models.IntegerField(default=0)
    type_reg = models.IntegerField(default=0)
    person_id = models.IntegerField(default=0)
    rule = models.IntegerField(default=0)
    lastgname = models.CharField(max_length=150, blank=True, default='')
    last_visit = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = u'registered_users'
        managed = False

class Schedule(models.Model):
    movie_id = models.ForeignKey(Movie, db_column='movie_id', on_delete = models.PROTECT)
    film_id = models.ForeignKey(Film, db_column='film_id', on_delete = models.PROTECT)
    hall_id = models.ForeignKey(AfishaHalls, db_column='hall_id', on_delete = models.PROTECT)
    date_from = models.DateField()
    date_to = models.DateField()
    autor = models.IntegerField()
    user_id = models.IntegerField()
    class Meta:
        db_table = u'schedule'
        managed = False

class SessionList(models.Model):
    priority = models.IntegerField()
    time = models.TextField()
    class Meta:
        db_table = u'session_list'
        managed = False

class AfishaSession(models.Model):
    schedule_id = models.ForeignKey(Schedule, db_column='schedule_id', on_delete = models.PROTECT)
    session_list_id = models.ForeignKey(SessionList, db_column='session_list_id', on_delete = models.PROTECT)
    price1 = models.IntegerField()
    price2 = models.IntegerField()
    kinohod = models.IntegerField()
    class Meta:
        db_table = u'session'
        managed = False

class CheckEditors(models.Model):
    field_id = models.IntegerField()
    user_id = models.IntegerField()
    action = models.IntegerField()
    date = models.DateTimeField()
    start = models.TextField()
    finish = models.TextField()
    status = models.IntegerField()
    check = models.IntegerField()
    rem = models.TextField()
    object_id = models.IntegerField()
    money = models.FloatField()
    user_ip = models.CharField(max_length=12)
    class Meta:
        db_table = u'check_editors'
        managed = False

class AfishaNews(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    annotation = models.CharField(max_length=255, blank=True, default='')
    type = models.IntegerField()
    object_type = models.IntegerField()
    obj = models.ForeignKey(Film, db_column='object', on_delete = models.PROTECT)
    user = models.ForeignKey(RegisteredUsers, db_column='user', on_delete = models.PROTECT)
    ip = models.CharField(max_length=12, blank=True, default='')
    read_all = models.IntegerField(default=0)
    read_yes = models.IntegerField(default=0)
    read_no = models.IntegerField(default=0)
    class Meta:
        db_table = u'news'
        managed = False

class GGOpinion(models.Model):
    parent_id = models.IntegerField()
    branch_id = models.IntegerField()
    user_id = models.ForeignKey(RegisteredUsers, db_column='user_id', null=True, on_delete = models.PROTECT)
    date = models.DateTimeField()
    text = models.TextField()
    subject	= models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    nick = models.CharField(max_length=25)
    first = models.IntegerField()
    type_obj = models.IntegerField()
    locked = models.IntegerField()
    type = models.IntegerField()
    deleted	= models.IntegerField()
    obj_id = models.IntegerField()
    ip = models.CharField(max_length=15)
    class Meta:
        db_table = u'gg_opinion'
        managed = False

class TrailerInfo(models.Model):
    trailer_id = models.IntegerField(primary_key=True, db_column='TrailerID')
    group_id = models.IntegerField(db_column='GroupID')
    date = models.DateField(db_column='Date')
    size_w = models.IntegerField(db_column='Size_W')
    size_h = models.IntegerField(db_column='Size_H')
    runtime = models.IntegerField(db_column='RunTime')
    cmt = models.TextField(db_column='Cmt', blank=True)
    cmt_group = models.TextField(db_column='Cmt_Group')
    file_ext = models.CharField(max_length=5, db_column='FileExt', blank=True)
    code = models.CharField(max_length=1023, db_column='Code')
    class Meta:
        db_table = u'TrailerInfo'
        managed = False

class FilmsRamb(models.Model):
    id_source = models.IntegerField(db_column='id_source', null=True)
    id_film = models.ForeignKey(Film, db_column='id_film', null=True, on_delete = models.PROTECT)
    id_out = models.IntegerField(db_column='id_out', null=True)
    class Meta:
        db_table = u'films_ramb'
        managed = False

class ImportCinema(models.Model):
    cinema_id = models.IntegerField(db_column='Cinema_ID')
    cinema_name = models.CharField(max_length=80, db_column='Cinema_Name')
    script_id = models.IntegerField(db_column='Script_ID')
    text_ord = models.TextField(db_column='Text_Ord')
    sms_word = models.CharField(max_length=31, db_column='sms_word')
    class Meta:
        db_table = u'import_cinema'
        managed = False

class FilmsCodes(models.Model):
    film = models.ForeignKey(Film, db_column='film_id', null=True, on_delete = models.PROTECT)
    player = models.TextField(db_column='player', null=True, blank=True)
    class Meta:
        db_table = u'films_codes'
        managed = False

class Gathering(models.Model):
    week_num = models.IntegerField(db_column='week_num')
    friday_date = models.DateField(db_column='friday_date')
    sunday_date = models.DateField(db_column='sunday_date')
    place = models.IntegerField(db_column='place')
    film = models.ForeignKey(Film, db_column='film_id', on_delete = models.PROTECT)
    period_gathering = models.IntegerField(db_column='period_gathering')
    total_gathering = models.IntegerField(db_column='total_gathering')
    country = models.ForeignKey(AfishaCountry, db_column='country_id', on_delete = models.PROTECT)
    date_from = models.IntegerField(db_column='date_from')
    date_to = models.IntegerField(db_column='date_to')
    day_in_rent = models.IntegerField(db_column='day_in_rent')
    class Meta:
        db_table = u'gathering'
        managed = False


class WFOpinion(models.Model):
    parent = models.IntegerField(db_column='parent_id', default=0)
    branch = models.IntegerField(db_column='branch_id', default=0)
    user = models.ForeignKey(RegisteredUsers, db_column='user_id', default=0, null=True, on_delete = models.PROTECT)
    date = models.DateTimeField(db_column='date', auto_now_add=True)
    text = models.TextField(db_column='text')
    subject = models.CharField(max_length=255, db_column='subject', default='')
    email = models.CharField(max_length=50, db_column='email', default='')
    nick = models.CharField(max_length=25, db_column='nick', default='')
    first = models.BooleanField(db_column='first', default=False)
    type_obj = models.IntegerField(db_column='type_obj', default=1)
    locked = models.BooleanField(db_column='locked', default=False)
    type = models.IntegerField(db_column='type', default=0)
    deleted = models.BooleanField(db_column='deleted', default=False)
    anonim = models.BooleanField(db_column='anonim', default=False)
    other = models.CharField(max_length=8, db_column='other', default='0000000')
    class Meta:
        db_table = u'wf_opinion'
        managed = False

class WFStat(models.Model):
    opinion = models.IntegerField(db_column='opinion_id', default=0)
    count = models.IntegerField(db_column='count', default=0)
    date = models.DateTimeField(db_column='date', auto_now_add=True)
    class Meta:
        db_table = u'wf_stat'
        managed = False

class WFUser(models.Model):
    user = models.IntegerField(db_column='user_id', default=0)
    opinion = models.IntegerField(db_column='opinion_id', default=0)
    date = models.DateTimeField(db_column='date', auto_now_add=True)
    class Meta:
        db_table = u'wf_user'
        managed = False
