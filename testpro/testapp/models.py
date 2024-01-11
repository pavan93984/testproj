from django.db import models
from django.urls import reverse

# Create your models here.
class product_details(models.Model):
    product_name = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    img = models.ImageField(upload_to="userimage/",blank=True)

    
    def __str__(self):
        return self.product_name
    

class Bills(models.Model):
    product = models.ForeignKey("product_details",related_name="product",on_delete=models.CASCADE)
    materil = models.ForeignKey("product_details",related_name="materials",on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    price = models.IntegerField()

    
    

