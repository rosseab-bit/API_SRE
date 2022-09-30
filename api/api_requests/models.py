from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class DataFly(models.Model):
    fecha_i = models.CharField(max_length=150)
    vlo_i = models.IntegerField()
    ori_i = models.CharField(max_length=150)
    des_i = models.CharField(max_length=150)
    emp_i = models.CharField(max_length=150)
    fecha_o = models.CharField(max_length=150)
    vlo_o = models.CharField(max_length=150)
    ori_o = models.CharField(max_length=150)
    des_o = models.CharField(max_length=150)
    emp_o = models.CharField(max_length=150)
    day_month = models.IntegerField()
    month_fly = models.IntegerField()
    year_fly = models.IntegerField()
    day_fly = models.IntegerField()
    type_fly = models.CharField(max_length=2)
    enterprice = models.CharField(max_length=200)
    siglaori = models.CharField(max_length=200)
    siglades = models.CharField(max_length=200)




# (fecha_i = "05092022", vlo_i=1, ori_i="buenos aires", des_i="cordoba", emp_i="aerolineas", fecha_o="05092022", vlo_o="n2m31nzx3", ori_o="bsas", des_o="co", emp_o="al", day_month=5, month_fly=9, year_fly=2022, day_fly=2, type_fly="N", enterprice="aerolineas argentina", siglaori="caba", siglades="jesus maria")
