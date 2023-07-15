from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50 , unique=True)
    slug  = models.SlugField(max_length=100 , unique=True)
    description =models.TextField(max_length=255 , blank=True)
    cat_image = models.ImageField(upload_to = 'photoes/categories' ,blank=True)
    #api additional dewal ape data base ekata denna thamai meta kiyana eka use karanne  
    class Meta:
        verbose_name = 'caregory'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.category_name
    