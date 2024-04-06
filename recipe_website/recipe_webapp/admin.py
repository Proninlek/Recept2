from django.contrib import admin
from recipe_webapp.models import Recipe, RecipeCategory, Category

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'cooking_time', 'weight')
    search_fields = ['title', 'author', 'ingredients']
    list_filter = ('cooking_time', 'author')

admin.site.register(Category)
admin.site.register(RecipeCategory)


admin.site.register(Recipe, RecipeAdmin)
