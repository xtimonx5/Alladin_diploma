from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group, Permission


class Company(models.Model):
    name = models.CharField(max_length=50)

    # Address
    city = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=30, null=True, blank=True)
    street = models.CharField(max_length=30, null=True, blank=True)

    owner = models.ForeignKey(User, related_name='user')

    @staticmethod
    def post_save_from_user(sender, **kwargs):
        instance = kwargs.get('instance')
        created = kwargs.get('created')
        if created:
            Company.objects.create(name=instance.username + ' company', owner=instance)
            instance.is_staff = True
            instance.save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company'


post_save.connect(Company.post_save_from_user, sender=User)
