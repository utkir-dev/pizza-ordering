from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

from projectPizza.models import Category, Pizza,PizzaNumber

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

class PizzaAdmin(admin.ModelAdmin):
    list_display=['title','slug','created_at',]
    prepopulated_fields={'slug':('title',)}
class PizzaNumberAdmin(admin.ModelAdmin):
    list_display=['branches','awards','customer','staff']

admin.site.register(PizzaNumber,PizzaNumberAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Pizza,PizzaAdmin)
admin.site.unregister(Group)
