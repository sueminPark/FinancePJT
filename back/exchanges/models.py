from django.db import models
from django.conf import settings


# Create your models here.
class Exchange(models.Model):
    cur_unit = models.TextField(max_length=10)
    cur_nm = models.TextField()
    deal_bas_r = models.TextField()

