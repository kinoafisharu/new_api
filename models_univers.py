# Здесь будут модели универсальных объектов: годы, страны, города и др. 
class BaseCity(models.Model):
    phone_code = models.IntegerField(blank=True, null=True)
    kid = models.BigIntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_city'


class BaseCityName(models.Model):
    city_id = models.IntegerField()
    namecity_id = models.IntegerField()

    class Meta:
        db_table = 'base_city_name'
        unique_together = (('city_id', 'namecity_id'),)

