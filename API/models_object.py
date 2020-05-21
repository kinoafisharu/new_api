# здесь будут модели объектов Фильм, Персона, Организация и др.

'''
ФИЛЬМ
'''
# названия Фильма (связь с NaneFilms)
class BaseFilmsName(models.Model):
    films_id = models.IntegerField()
    namefilms_id = models.IntegerField()

    class Meta:
        db_table = 'base_films_name'
        unique_together = (('films_id', 'namefilms_id'),)

# собственно названия (статусы: 1 - основное, 2 - сжатое, 3 - альтернативное;
#                      ид языка: 1 - английский, 2 - русский (вижу в БД поломку, почти у всех - 2)
class BaseNamefilms(models.Model):
    status = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_namefilms'

# модель 1 из 4 идентифицирующих Фильм (пока пустая, наполнить с IMDb)
class BaseFilmsProduction(models.Model):
    films_id = models.IntegerField()
    productionsco_id = models.IntegerField()

    class Meta:
        db_table = 'base_films_production'
        unique_together = (('films_id', 'productionsco_id'),)

# модель 2  (жанры) из 4 идентифицирующих Фильм      
class BaseFilmsGenre(models.Model):
    films_id = models.IntegerField()
    genre_id = models.IntegerField()

    class Meta:
        db_table = 'base_films_genre'
        unique_together = (('films_id', 'genre_id'),)

#  названия жанров (и связь с киноафишей)       
class BaseGenre(models.Model):
    name = models.CharField(max_length=64)
    name_en = models.CharField(max_length=64, blank=True, null=True)
    kid = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_genre'


        
# часть слоя IMDb (позже соединить в один общий слой или заменить на считывание "на лету" (но с кэшем)       
class BaseImdb(models.Model):
    id_imdb = models.BigIntegerField()
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'base_imdb'

# связь с таблицей дат релизов        
class BaseFilmsRelease(models.Model):
    films_id = models.IntegerField()
    filmsreleasedate_id = models.IntegerField()

    class Meta:
        db_table = 'base_films_release'
        unique_together = (('films_id', 'filmsreleasedate_id'),)

# даты релизов (+ примечание к релизу, формат релиза (кино, онлайн-платформы и т.п.), страна релиза
class BaseFilmsreleasedate(models.Model):
    release = models.DateField()
    note = models.CharField(max_length=256, blank=True, null=True)
    format = models.CharField(max_length=1) # ключевое слово Джанго???
    country_id = models.IntegerField()

    class Meta:
        db_table = 'base_filmsreleasedate'

# бюджет фильма (почему киноафишная связь?)
class BaseFilmsbudget(models.Model):
    kid = models.IntegerField()
    budget = models.CharField(max_length=64)

    class Meta:
        db_table = 'base_filmsbudget'

# связь фильма с источниками?        
class BaseFilmssources(models.Model):
    id_films_id = models.IntegerField()
    source_id = models.IntegerField()
    id_films_sources = models.BigIntegerField()

    class Meta:
        db_table = 'base_filmssources'

# киноафишные оценки юзеров
class BaseFilmsvotes(models.Model):
    kid = models.IntegerField()
    user_id = models.IntegerField()
    rate_1 = models.IntegerField()
    rate_2 = models.IntegerField()
    rate_3 = models.IntegerField()

    class Meta:
        db_table = 'base_filmsvotes'


# этот класс описывает ту часть объекта Фильм, которая собрала пока несистемные свойства фильма
class BaseFilms(models.Model):
    year = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True) #(ключевое слово Джанго!!!)
    runtime = models.IntegerField(blank=True, null=True)
    rated = models.IntegerField(blank=True, null=True)
    budget_id = models.IntegerField(blank=True, null=True)
    imdb_id = models.IntegerField(blank=True, null=True)
    imdb_rate = models.FloatField(blank=True, null=True)
    imdb_votes = models.IntegerField(blank=True, null=True)
    kid = models.IntegerField(blank=True, null=True)
    generated = models.IntegerField()
    generated_dtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'base_films'
        
    '''
    ПЕРСОНА
    '''
# модель имен персон (вынести с персонами вместе в корень)
class BaseNameperson(models.Model):
    status = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_nameperson'
        
# модель персон (вынести в корень)
class BasePerson(models.Model):
    iid = models.BigIntegerField(blank=True, null=True)
    kid = models.BigIntegerField(blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    born = models.DateField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    artist = models.IntegerField()
    is_group = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    video = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'base_person'

    
    '''
    ОРГАНИЗАЦИЯ
    '''
