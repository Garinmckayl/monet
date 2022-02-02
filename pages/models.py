from multiprocessing.spawn import import_main_path
from operator import mod

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE
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


class Bid(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE, null=False, default='1')
    auction = models.ForeignKey(Auction, on_delete=CASCADE, null=False, default='1')
    bid_price = models.IntegerField(null=False, default='1000')
    bid_time = models.TimeField(null=False, default='00:00:00')

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE, null=False, default='1')
    auction = models.ForeignKey(Auction, on_delete=CASCADE, null=False, default='1')
    comments = models.CharField(max_length=150, default='abc')

class Watchlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=CASCADE,)
    auction = models.ForeignKey(Auction, on_delete=CASCADE)
    active = models.BooleanField(default=False)
