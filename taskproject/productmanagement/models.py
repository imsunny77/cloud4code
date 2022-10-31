from django.db import models
from taskproject.models import BaseModel

# Create your models here.
class ProductCategory(BaseModel):
    parent_category = models.ForeignKey('self', on_delete= models.CASCADE, null=True,blank=True)
    category = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return str(self.category.capitalize())



    def save(self, *args, **kwargs):
        self.category = (self.category.lower())
        super(ProductCategory, self).save(*args, **kwargs)

class Product(BaseModel):
    product_name = models.CharField(max_length=100, null=True)
    product_category = models.ForeignKey(ProductCategory, on_delete= models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField( null=True, blank=True)
    feature_image = models.FileField(upload_to='product/feature-image/', null=True)

    def __str__(self):
        return str(self.id)

    def category_name(self):
            return self.product_category.category

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete= models.CASCADE, null=True)
    image = models.ImageField(upload_to='product/image/', null=True)

    def __str__(self):
        return str(self.id)
