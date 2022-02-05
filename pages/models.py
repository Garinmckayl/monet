from multiprocessing.spawn import import_main_path
from operator import mod
from platform import platform
from pyexpat import model
from statistics import mode

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from accounts.models import Company, CustomUser


class Category(models.Model):
    category = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.category

class Auction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, default='1')
    company = models.OneToOneField(Company, on_delete=CASCADE)
    description = models.CharField(max_length=100, null=False, default='description')
    starting_price = models.IntegerField(null=False , default='123')
    category = models.ForeignKey(Category, on_delete=CASCADE, null=False, default='1')
    active = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('auction-detail', kwargs={'pk':self.pk})
class Bid(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE, null=False, default='1')
    auction = models.ForeignKey(Auction, on_delete=CASCADE, null=False, default='1')
    bid_price = models.IntegerField(null=False, default='1000')
    bid_time = models.TimeField(null=False, default=timezone.now)



class Watchlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE,)
    auction = models.ForeignKey(Auction, on_delete=CASCADE)
    active = models.BooleanField(default=False)


class DataSource(models.Model):

    ''' will hold revenue information'''

#     {'id': '4f3b3664-7c14-4dc4-921a-8a6353e11b5d',
#    'name': 'Recipe test company',
#    'platform': 'Sandbox',
#    'redirect': 'https://link.codat.io/company/4f3b3664-7c14-4dc4-921a-8a6353e11b5d',
#    'lastSync': '2022-02-02T21:48:33.6473283Z',
#    'dataConnections': [{'id': 'b33249b2-7cb0-405e-b4ad-14661f2f2813',
#      'integrationId': '9e0cc03b-3868-4543-98c0-568f0f1b12a3',
#      'sourceId': 'aff0f057-255f-42c4-8d4a-ae23b43e1615',
#      'platformName': 'Sandbox',
#      'linkUrl': 'https://link-api.codat.io/companies/4f3b3664-7c14-4dc4-921a-8a6353e11b5d/connections/b33249b2-7cb0-405e-b4ad-14661f2f2813/start',
#      'status': 'Linked',
#      'lastSync': '2022-02-02T21:48:33.6473281Z',
#      'created': '2022-02-02T21:47:56Z',
#      'sourceType': 'Accounting'}],
#    'created': '2022-02-02T21:47:03Z'}

    company= models.OneToOneField(Company, on_delete=CASCADE)
    codat_id = models.CharField(max_length=255, unique=True)
    platform = models.CharField(max_length=100)# platform name like Sandbox
    redirect= models.URLField()
    last_sync= models.DateTimeField(null=True)
    status= models.CharField(max_length=100)
    
    created = models.DateTimeField(default=timezone.now())
