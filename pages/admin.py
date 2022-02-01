from django.contrib import admin

from pages.models import Auction, Category


class AuctionAdmin(admin.ModelAdmin):
    
    list_display = [field.name for field in Auction._meta.fields]

class CategoryAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Category._meta.fields]


admin.site.register(Auction, AuctionAdmin)

admin.site.register(Category, CategoryAdmin)