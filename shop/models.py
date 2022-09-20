from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='NameSurname', unique=True)


    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length=20, verbose_name='NameofProduct', unique=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)