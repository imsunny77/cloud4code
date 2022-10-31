from rest_framework import serializers
from .models import *

 
class ParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id','category',]

class ProductCategorySerializer(serializers.ModelSerializer):
    parent_category =  ParentCategorySerializer(read_only=True)
    class Meta:
        model = ProductCategory
        fields = ['id','parent_category','category',]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','product_name', 'product_category', 'price', 'feature_image', 'description','category_name']

