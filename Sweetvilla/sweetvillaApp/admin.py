from django.contrib import admin
from.models import Product
class productadmin(admin.ModelAdmin):
   pass

# Register your models here.
admin.site.register(Product,productadmin)

# Register your models here.
