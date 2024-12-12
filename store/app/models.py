from django.db import models

# Create your models here.
class Category(models.Model):
     cat_name=models.TextField()

class Product(models.Model):
     pid=models.TextField()
     name=models.TextField()
     disc=models.TextField()
     price=models.IntegerField()
     offer_price=models.IntegerField()
     img=models.FileField()
     cat_id=models.ForeignKey(Category,on_delete=models.CASCADE)

class Weight(models.Model):
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     product_weight=models.TextField()
     stock=models.IntegerField()

