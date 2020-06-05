from django.test import TestCase
from . import models
from . import serializers
import io

class ModelMethodsTest(TestCase):
    def model_films_doesnt_save_when_year_less_than_0(self):
        c = models.Films.objects.create(year = 2000, runtime = -200)
        self.assertEqual(None, c)
