from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=50)

    # Address
    city = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=30, null=True, blank=True)
    street = models.CharField(max_length=30, null=True, blank=True)

    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    owner = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
