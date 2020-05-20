# здесь будут модели объектов Фильм, Персона, Организация и др.

'''
ФИЛЬМ
'''

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
        
    '''
    ПЕРСОНА
    '''
    
    '''
    ОРГАНИЗАЦИЯ
    '''
