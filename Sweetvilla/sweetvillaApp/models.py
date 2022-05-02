from itertools import product
from django.db import models
class Product(models.Model):
    prodname=models.CharField(("productName "), max_length=50)
    cetegory=models.CharField(("Cetegory"), max_length=60,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(("Description"), max_length=300)
    publish_date=models.DateField(("publishDate"))
    images=models.ImageField(("Images"), upload_to='EcommerceApp/images',default="")
    def __str__(self):
      return self.prodname
# Create your models here.

