from django.db import models

from shop.models.products import save
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveBigIntegerField(default=0)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    discount_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):

        if self.discount > 0:
            self.discount_price = self.price - self.price*self.discount/100

        super().save(*args, **kwargs)
    
    
