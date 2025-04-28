# models.py
# from django import *
from django.db import models
import settings
# from TestModel import models

class Test(models.Model):
    id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

Test.objects.create(id=12,name='abc123')

Test.objects.all()#查询表中的所有记录

