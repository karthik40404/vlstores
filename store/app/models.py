from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
     cat_name=models.TextField()
     cat_image=models.FileField()

class Product(models.Model):
     pid=models.TextField()
     name=models.TextField()
     disc=models.TextField()
     img=models.FileField()
     cat_id=models.ForeignKey(Category,on_delete=models.CASCADE)

class Weight(models.Model):
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     price=models.IntegerField()
     offer_price=models.IntegerField()
     product_weight=models.TextField()
     stock=models.IntegerField()

