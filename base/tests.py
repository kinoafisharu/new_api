from django.test import TestCase
from . import models
from . import serializers
from rest_framework.parsers import JSONparser
import io

# class ValidationTest(TestCase):
    # def serialize_valid_data_and_create_objects(self):
        # with open(*path_to_json_with_test_data*) as j:
            # stream = io.BytesIO(j)
            # data = JSONParser.parse(stream)
            # serializer = BaseFilmsSerializer(data = data)
            # self.assertTrue(serializer.is_valid())
            # if seriaizer.is_valid():
                # serializer.save()

                
