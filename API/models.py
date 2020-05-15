from django.db import models
# справочники: страны, годы, жанры, источники киноданных, возр.ограничения, языки, профессии
# объекты: названия локализованные, названия международные, названия оригинальные, фильмы, организации, люди
# процессы: оценки, мнения, подписки, сеансы

class Film(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    title_local = models.ForeignKey(FilmNamesLocal)
    title_int = models.ForeignKey(FilmNamesInt)
    title_orig = models.ForeignKey(FilmNamesOrig)
    country = models.ForeignKey(Country)
