from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Only use auto_now_add

    def __str__(self):
        return self.title
