from django.db import models

# Create your models here.


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    preparation_steps = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="время в минутах")
    ingredients = models.TextField()
    images = models.ImageField(upload_to='recipe_images/', blank=True)
    author = models.CharField(max_length=128)
    weight = models.PositiveIntegerField(help_text="вес в граммах")
class Category(models.Model):
    name = models.CharField(max_length=128)

class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
