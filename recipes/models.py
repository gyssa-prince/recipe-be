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
    posted_by = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Only use auto_now_add

    def __str__(self):
        return self.title
    
class LandingPageContent(models.Model):
    hero_title = models.CharField(max_length=200, default="Welcome to Our Platform!")
    hero_description = models.TextField(
        default=(
            "We’re thrilled to have you join our vibrant community of food lovers, home cooks, "
            "and culinary explorers. Whether you’re here to share your favorite recipes, discover "
            "new flavors, or connect with fellow food enthusiasts, your journey to culinary greatness starts here."
        )
    )
    hero_button_text = models.CharField(max_length=50, default="Get Started")
    hero_image = models.ImageField(upload_to="landing_page/", blank=True, null=True)

    about_title = models.CharField(max_length=200, default="About Us")
    about_description = models.TextField(
        default=(
            "At ShareRecipe, we’re passionate about bringing people together through the joy of cooking. "
            "Our mission is to create a welcoming space where food lovers can share, discover, and celebrate "
            "recipes from around the world. Whether you’re a seasoned chef or a kitchen newbie, we’re here to inspire your culinary journey."
        )
    )

    feature_title = models.CharField(max_length=200, default="Our Features")

    def __str__(self):
        return "Landing Page Content"