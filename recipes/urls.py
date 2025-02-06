from django.urls import path
from .views import (
    RecipeListView, 
    RecipeDetailView, 
    CategoryListView, 
    CategoryDetailView,
    LandingPageContentView,  # Ensure this import is correct
)

urlpatterns = [
    # Recipe URLs
    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),

    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    # Landing Page Content URL
    path('landing-page-content/', LandingPageContentView.as_view(), name='landing-page-content'),  # Ensure the trailing slash is present
]