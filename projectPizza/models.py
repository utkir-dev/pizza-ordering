from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    """ Model for Category"""
    name=models.CharField(max_length=255, null=False,blank=False,unique=True,error_messages={"unique":"Bu nom allaqachon mavjud!"})
    slug=models.SlugField(max_length=255, null=False,blank=True, unique=True,error_messages={"unique":"Bu slug allaqachon mavjud!"})
    
    def get_absolute_url(self):
        return reverse('myapp:pizza_list_by_category',args=[self.slug])
    class Meta:
        verbose_name="Category"
        verbose_name_plural="Category"

    def __str__(self) :
        for_admin=f"{self.name} {self.slug}"
        return for_admin
    

class Pizza(models.Model):
    """Model ofr Pizza"""
    category=models.ForeignKey(Category,on_delete=models.CASCADE)  # category o'chsa pizza ham o'chib ketadi
    # category=models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)  # category o'chsa pizza o'chmaydi
    # category=models.ForeignKey(Category,on_delete=models.SET_DEFAULT) 
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    slug=models.SlugField(max_length=255, null=False,blank=True, unique=True,error_messages={"unique":"Bu slug allaqachon mavjud!"})
    image=models.ImageField(upload_to="Pizza/")
    update=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('myapp:pizza_detail',args=[self.id,self.slug])


    class Meta:
        verbose_name="Pizza"
        verbose_name_plural="Pizza"

    def __str__(self):
        for_admin=f"{self.title} {self.price} {self.created_at}"
        return for_admin

class PizzaNumber(models.Model):
    branches=models.PositiveIntegerField(default=1)
    awards=models.PositiveIntegerField(default=1)
    customer=models.PositiveIntegerField(default=1)
    staff=models.PositiveIntegerField(default=1)


    class Meta:
        verbose_name="Pizza Number"
        verbose_name_plural="Pizza Number"

    def __str__(self):
        for_admin=f"{self.branches} {self.awards} {self.customer}"
        return for_admin
    
class Chef(models.Model):
    name=models.CharField(max_length=100)    
    surname=models.CharField(max_length=100)  
    specialist=models.CharField(max_length=100)  
    description=models.TextField() 
    image=models.ImageField(upload_to='chef/')
    update=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Chef"
        verbose_name_plural="Chef"

    def __str__(self):
        for_admin=f"{self.name} {self.surname} {self.specialist}"
        return for_admin
    
    def full_name(self):
        return self.name + " " + self.surname