from __future__ import unicode_literals
from django.db import models

BOOL_CHOICES = ((True, 'true'), (False, 'false'))
# Create your models here.
class Calc(models.Model):
    distance = models.FloatField(default=0)
    isMeters = models.BooleanField(default=True)

    def __str__(self):
        return self.distance
