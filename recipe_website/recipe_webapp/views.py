from random import sample

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from Recipe_website.forms import RecipeForm
from recipe_webapp.models import Recipe


# Create your views here.


def home(request):
    recipes = list(Recipe.objects.all())
    featured_recipes = sample(recipes, min(len(recipes), 5)) if recipes else []
    return render(request, 'base.html', {'recipes': featured_recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'detailed_recipe.html', {'recipe': recipe})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'regestration.html', {'form': form})

def any_recipe(request):
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'any_recipe.html', {'recipes': recipes})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

class RecipeEditView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_edit.html'

    success_url = reverse_lazy('any_recipe')

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'

    success_url = reverse_lazy('any_recipe')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author != request.user:
        raise Http404
    if request.method == 'POST':
        form = Recipe(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = Recipe(instance=recipe)
    return render(request, 'recipe_form.html', {'form': form})