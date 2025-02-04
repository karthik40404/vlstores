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

class Cart(models.Model):
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     weight=models.ForeignKey(Weight,on_delete=models.CASCADE)
     qty=models.IntegerField()

class Buy(models.Model):
    PAYMENT_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('online', 'Online Payment'),
    ]
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    weight=models.ForeignKey(Weight,on_delete=models.CASCADE)
    qty=models.IntegerField()
    total_price=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='cod')
    billing_address = models.TextField(blank=True, null=True)
