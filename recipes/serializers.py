# serializers.py
from rest_framework import serializers
from .models import Recipe, Category

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'  # or specify the fields explicitly, e.g., ['id', 'title', 'category', 'posted_by', 'description', 'image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # or specify the fields explicitly, e.g., ['id', 'name', 'description']