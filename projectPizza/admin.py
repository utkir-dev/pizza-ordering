from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

from projectPizza.models import Category, Pizza,PizzaNumber,Chef

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

class PizzaAdmin(admin.ModelAdmin):
    list_display=['title','slug','created_at',]
    prepopulated_fields={'slug':('title',)}
    
class PizzaNumberAdmin(admin.ModelAdmin):
    list_display=['branches','awards','customer','staff']


class ChefAdmin(admin.ModelAdmin):
    list_display=['name','surname','specialist','created_at']

admin.site.register(Chef,ChefAdmin)    
admin.site.register(PizzaNumber,PizzaNumberAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Pizza,PizzaAdmin)
admin.site.unregister(Group)
