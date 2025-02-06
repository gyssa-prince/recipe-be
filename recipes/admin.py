from django.contrib import admin
from .models import Recipe, Category
from .models import LandingPageContent

admin.site.register(Recipe)
admin.site.register(Category)
@admin.register(LandingPageContent)
class LandingPageContentAdmin(admin.ModelAdmin):
    list_display = ["id", "hero_title", "about_title", "feature_title"]
    search_fields = ["hero_title", "about_title", "feature_title"]
    list_editable = []  # Add fields here if you want them to be directly editable in the admin list view.