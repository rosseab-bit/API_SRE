from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class DataFly(models.Model):
    fecha_i = models.CharField(max_length=150)
    vlo_i = models.IntegerField(max_length=150)
    ori_i = models.CharField(max_length=150)
    des_i = models.CharField(max_length=150)
    emp_i = models.CharField(max_length=150)
    fecha_i = models.CharField(max_length=150)
    vlo_o = models.CharField(max_length=150)
    ori_o = models.CharField(max_length=150)
    des_o = models.CharField(max_length=150)
    emp_o = models.CharField(max_length=150)
    day_month = models.IntegerField(max_length=150)
    month_fly = models.IntegerField(max_length=150)
    year_fly = models.IntegerField(max_length=150)
    day_fly = models.IntegerField(max_length=150)
    type_fly = models.CharField(max_length=2)
    enterprice = models.CharField(max_length=200)
    siglaori = models.CharField(max_length=200)
    siglades = models.CharField(max_length=200)

