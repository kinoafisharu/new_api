# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.sites.models import Site as DjangoSite
from base.models_choices import *

"""
Модели - справочники
"""

class Language(models.Model):
    name = models.CharField(max_length=64, verbose_name='Язык')
    code = models.CharField(max_length=8, verbose_name='Код')
    def __unicode__(self):
        return '%s' % (self.name)

class Country(models.Model):
    name = models.CharField(max_length=64, verbose_name='Страна')
    name_en = models.CharField(max_length=64, verbose_name='Англ. название страны для GeoIP')
    kid = models.BigIntegerField(verbose_name='ID города у источника')
    class Meta:
        ordering = ['name']
    def __unicode__(self):
        return '%s' % (self.name)

class LanguageCountry(models.Model):
    '''
    Язык страны - справочник
    '''
    language = models.ForeignKey(Language, on_delete = models.PROTECT)
    country = models.ForeignKey(Country, on_delete = models.PROTECT)


class NameCity(models.Model):
   '''
   Названия городов
   '''
   status = models.IntegerField(verbose_name='Статус имени (1 - главное, 0 - альт, 2 - очищ, 3 - род.падеж)', db_index=True)
   language = models.ForeignKey(Language, blank=True, null=True, on_delete = models.PROTECT)
   name = models.CharField(max_length=256, verbose_name='Название')
   class Meta:
       verbose_name = u'Название'
       verbose_name_plural = u'Названия'
   def __unicode__(self):
       return '%s' % self.name

class NameCinema(models.Model):
   '''
   Названия кинотеатров
   '''
   status = models.IntegerField(verbose_name='Статус имени (1 - главное, 0 - альтернативное, 2 - очищенное)', db_index=True)
   language = models.ForeignKey(Language, blank=True, null=True, on_delete = models.PROTECT)
   name = models.CharField(max_length=256, verbose_name='Название')
   class Meta:
       verbose_name = u'Название'
       verbose_name_plural = u'Названия'
   def __unicode__(self):
       return '%s' % self.name

class NameHall(models.Model):
   '''
   Названия залов
   '''
   status = models.IntegerField(verbose_name='Статус имени (1 - главное, 0 - альтернативное, 2 - очищенное)')
   language = models.ForeignKey(Language, blank=True, null=True, on_delete = models.PROTECT)
   name = models.CharField(max_length=256, verbose_name='Название')
   class Meta:
       verbose_name = u'Название'
       verbose_name_plural = u'Названия'
   def __unicode__(self):
       return '%s' % self.name


class Area(models.Model):
    '''
    Регион, область, район
    '''
    name = models.CharField(max_length=256, verbose_name='Название')
    slug = models.CharField(max_length=256, verbose_name='Очищенное название')

    def __unicode__(self):
       return '%s' % self.name


class City(models.Model):
    name = models.ManyToManyField(NameCity, verbose_name='Город', blank=True, null=True)
    phone_code = models.IntegerField(verbose_name='Телефонный код города', blank=True, null=True)
    kid = models.BigIntegerField(verbose_name='ID города у источника')
    country = models.ForeignKey(Country, blank=True, null=True, on_delete = models.PROTECT)

    def __unicode__(self):
        return '%s' % (self.name)


class Street(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    slug = models.CharField(max_length=64, verbose_name='Slug')
    type = models.CharField(max_length=2, choices=STREET_TYPE_CHOICES, verbose_name='Тип улицы')
    area = models.ForeignKey(Area, null=True, on_delete = models.PROTECT)

class Building(models.Model):
    city = models.ForeignKey(City, verbose_name='Город', null=True, on_delete = models.PROTECT)
    street = models.ForeignKey(Street, verbose_name='Улица', null=True, on_delete = models.PROTECT)
    number = models.CharField(max_length=8, verbose_name='Дом', null=True)
    path = models.TextField(verbose_name='Путь', null=True, blank=True)

class StreetType(models.Model):
    name = models.CharField(max_length=64, verbose_name='Тип улицы')
    def __unicode__(self):
        return '%s' % (self.name)

class Metro(models.Model):
    name = models.CharField(max_length=64, verbose_name='Станция метро')
    kid = models.BigIntegerField(verbose_name='ID города у источника', null=True)
    def __unicode__(self):
        return '%s' % (self.name)

class CinemaCircuit(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название сети кинотеатров')
    kid = models.BigIntegerField(verbose_name='ID города у источника', null=True)
    def __unicode__(self):
        return '%s' % (self.name)

class Version(models.Model):
    name = models.CharField(max_length=64, verbose_name='Версия')
    def __unicode__(self):
        return '%s' % (self.name)

class Genre(models.Model):
    name = models.CharField(max_length=64, verbose_name='Жанр ru')
    name_en = models.CharField(max_length=64, verbose_name='Жанр en', null=True)
    kid = models.BigIntegerField(verbose_name='KID жанра', null=True)
    def __unicode__(self):
        return '%s' % (self.name)

class Runtime(models.Model):
    """
    Хронометраж версий - справочник
    """
    runtime = models.IntegerField(verbose_name='Хронометраж')
    runtime_note = models.TextField(verbose_name='Версия', blank=True, null=True)
    def __unicode__(self):
        return '%s' % (self.runtime)

class Budget(models.Model):
   '''
   Бюджет - справочник
   '''
   budget = models.BigIntegerField(verbose_name='Количество денег')
   currency = models.CharField(max_length=1, choices=CURRENCY_CHOICES, verbose_name='Валюта')

class ImageParameter(models.Model):
    '''
    Параметры изображения - справочник
    '''
    dimension = models.CharField(max_length=1, choices=DIMENSION_CHOICES,verbose_name='Число измерений')
    color = models.CharField(max_length=1, choices=COLOR_CHOICES, verbose_name='Цветность')
    aspect_ratio = models.CharField(max_length=1, choices=ASPECT_RATIO_CHOICES, verbose_name='Пропорции')

class SoundParameter(models.Model):
    '''
    Параметры звука - справочник
    '''
    sound = models.CharField(max_length=1, choices=SOUND_CHOICES,verbose_name='Число каналов')
    soundsystem = models.CharField(max_length=1, choices=SOUNDSYSTEM_CHOICES, verbose_name='Система звука')


# справочники персоны
class Action(models.Model):
    name = models.CharField(max_length=128, verbose_name='Тип участия персоны')
    def __unicode__(self):
        return '%s' % (self.name)

class StatusAct(models.Model):
    name = models.CharField(max_length=128, verbose_name='Статус участия персоны')
    def __unicode__(self):
        return '%s' % (self.name)

# справочники носителя
class CarrierType(models.Model):
    name = models.CharField(max_length=64, verbose_name='Тип носителя')
    def __unicode__(self):
        return '%s' % (self.name)

class CarrierLayer(models.Model):
    name = models.CharField(max_length=64, verbose_name='Тип(слойность) двд диска')
    def __unicode__(self):
        return '%s' % (self.name)

class CarrierRipType(models.Model):
    name = models.CharField(max_length=64, verbose_name='Тип РИПА на трекере')
    def __unicode__(self):
        return '%s' % (self.name)

class CarrierTapeCategorie(models.Model):
    name = models.CharField(max_length=64, verbose_name='Техническая категория кинопленки')
    def __unicode__(self):
        return '%s' % (self.name)

# справочники копии
class CopyFilmType(models.Model):
    name = models.CharField(max_length=128, verbose_name='Тип копии')
    def __unicode__(self):
        return '%s' % (self.name)

class CopyFilmFormat(models.Model):
    name = models.CharField(max_length=128, verbose_name='Формат изображения')
    def __unicode__(self):
        return '%s' % (self.name)

class CopyFilmAddValue(models.Model):
    name = models.CharField(max_length=128, verbose_name='доп.свойства издания (копии) типа “эконом” или “подарочный” или “региональный” или “комплект”')
    def __unicode__(self):
        return '%s' % (self.name)
