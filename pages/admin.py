from django.contrib import admin

from pages.models import Auction, Category, DataSource


class AuctionAdmin(admin.ModelAdmin):
    
    list_display = [field.name for field in Auction._meta.fields]

class CategoryAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Category._meta.fields]

class DatasourceAdmin(admin.ModelAdmin):

    list_display = [field.name for field in DataSource._meta.fields]


admin.site.register(Auction, AuctionAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(DataSource, DatasourceAdmin)