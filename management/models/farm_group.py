from django.db import models


class FarmGroup(models.Model):
    name = models.CharField(max_length=200)