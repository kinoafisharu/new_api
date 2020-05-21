from django.db import models


class BaseFilms(models.Model):
    year = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
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

    # Saving model instance to db if all the requirements are satisfied
    # def save(self, *args, **kwargs):
    #     if not self.imdb_votes:
    #         self.imdb_votes = round(self.imdb_rate / 2)
    #     if self.company_set or self.namelocalset or self.nameoriginal_set or self.nameinternational_set:
    #         super().save(*args, **kwargs)
    #     logger.warning('Model has not been saved , one of the necessary fields is missing')



class BaseNamefilms(models.Model):
    status = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_namefilms'

class BaseFilmsName(models.Model):
    films = models.ForeignKey(BaseFilms, db_column = 'films_id', on_delete = models.CASCADE)
    namefilms_id = models.ForeignKey(BaseNamefilms, db_column = 'namefilms_id', on_delete = models.CASCADE)

    class Meta:
        db_table = 'base_films_name'
        unique_together = (('films_id', 'namefilms_id'),)

class BaseGenre(models.Model):
    name = models.CharField(max_length=64)
    name_en = models.CharField(max_length=64, blank=True, null=True)
    kid = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_genre'


class BaseFilmsGenre(models.Model):
    films_id = models.ForeignKey(BaseFilms, db_column = 'films_id', on_delete = models.PROTECT)
    genre_id = models.ForeignKey(BaseGenre, db_column = 'genre_id', on_delete = models.PROTECT)

    class Meta:
        db_table = 'base_films_genre'
        unique_together = (('films_id', 'genre_id'),)

