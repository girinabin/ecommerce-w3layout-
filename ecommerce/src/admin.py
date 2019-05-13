from django.contrib import admin

from . models import Nut
from . models import Oil
from . models import Pasta_Noodle
class NutAdmin(admin.ModelAdmin):
    list_display = ['name','image','price','discount']
class OilAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'price', 'discount']
class Pasta_NoodleAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'price', 'discount']

# Register your models here.

admin.site.register(Nut,NutAdmin)
admin.site.register(Oil)
admin.site.register(Pasta_Noodle)
