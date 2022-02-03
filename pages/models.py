from multiprocessing.spawn import import_main_path
from operator import mod
from pyexpat import model

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE
from django.utils import timezone
from accounts.models import Company, CustomUser


class Category(models.Model):
    category = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return self.category

class Auction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, default='1')
    title = models.OneToOneField(Company, on_delete=CASCADE)
    description = models.CharField(max_length=100, null=False, default='ABC')
    starting_price = models.IntegerField(null=False , default='123')
    category = models.ForeignKey(Category, on_delete=CASCADE, null=False, default='1')
    active = models.BooleanField(null=False, default=False)
    created_at = models.DateTimeField(default=timezone.now)


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

    company= models.OneToOneField(Company, on_delete=CASCADE)
    codat_id = models.CharField(max_length=255, unique=True)
    url= models.URLField()
    created_at = models.DateTimeField(default=timezone.now())
