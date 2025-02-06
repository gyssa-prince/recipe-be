from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from .models import LandingPageContent

from .models import Recipe, Category
from .serializers import RecipeSerializer, CategorySerializer

# Existing Recipe views
class RecipeListView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetailView(APIView):
    def get(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response({'error': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response({'error': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response({'error': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)
        
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# New Category views
class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class LandingPageContentView(APIView):
    def get(self, request):
        content = LandingPageContent.objects.first()
        if not content:
            return Response({"error": "Landing page content not found"}, status=404)
        
        return Response({
            "hero_title": content.hero_title,
            "hero_description": content.hero_description,
            "hero_button_text": content.hero_button_text,
            "hero_image": content.hero_image.url if content.hero_image else None,
            "about_title": content.about_title,
            "about_description": content.about_description,
            "feature_title": content.feature_title,
            # Removed the "features" field
        })