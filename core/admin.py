from django.contrib import admin
from . models import *
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title','price','promo_price','avalable']

class PlatsAdmin(admin.ModelAdmin):
    list_display = ['title','menu','price','promo_price','avalable']
    ordering = ['-menu']
    

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','address_1','email','phone','date']

class Commande_MenuAdmin(admin.ModelAdmin):
    list_display = ['user','menu','status','date']

class Commande_PlatAdmin(admin.ModelAdmin):
    list_display = ['user','plat','status','date']

admin.site.register(Menu,MenuAdmin)
admin.site.register(Plats,PlatsAdmin)
admin.site.register(Commande_Menu,Commande_MenuAdmin)
admin.site.register(Commande_Plat,Commande_PlatAdmin)
admin.site.register(Pofile,ProfileAdmin)
