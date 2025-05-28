     # myapp/serializers.py
from rest_framework import serializers
from .models import Products, Categories # Import your model

class ProductsSerializer(serializers.ModelSerializer):
         class Meta:
             model = Products
             # Option 1: Include all fields
             fields = '__all__'
             # Option 2: Specify fields to include
             # fields = ['id', 'field1', 'field2', 'related_field']
             # Option 3: Specify fields to exclude
             # exclude = ['internal_field']
             
             # Optional: Make some fields read-only (e.g., id, owner)
             read_only_fields = ['id', 'owner'] 

class CategoriesSerializer(serializers.ModelSerializer):
       class Meta:
              model = Categories
              fields = '__all__'
