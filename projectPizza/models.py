from django.db import models
# Create your models here.

class Category(models.Model):
    """ Model for Category"""
    name=models.CharField(max_length=255, null=False,blank=False,unique=True,error_messages={"unique":"Bu nom allaqachon mavjud!"})
    slug=models.SlugField(max_length=255, null=False,blank=True, unique=True,error_messages={"unique":"Bu slug allaqachon mavjud!"})

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

    class Meta:
        verbose_name="Pizza"
        verbose_name_plural="Pizza"

    def __str__(self):
        for_admin=f"{self.title} {self.price} {self.created_at}"
        return for_admin
