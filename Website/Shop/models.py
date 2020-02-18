from django.db import models
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=256,unique=True)
    slug=models.SlugField(max_length=256,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='Category/',blank=True)

    class Meta:
        ordering=['name']
        verbose_name_plural='Categories'

    def get_url(self):
        return reverse('products_by_cat',args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=256,unique=True)
    slug=models.SlugField(max_length=256,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Product/',blank=True)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name_plural='Products'

    def __str__(self):
        return self.name
