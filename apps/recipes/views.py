from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView  
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm, RecipeForm
from .utils import generate_charts
import pandas as pd

def home(request):
  return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
  model = Recipe
  template_name = 'recipes/recipe_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipe
  template_name = 'recipes/recipe_detail.html'

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
  model = Recipe
  fields = ['name', 'ingredients', 'cooking_time', 'description', 'pic']
  template_name = 'recipes/recipe_update.html'

  def form_valid(self, form):
        name = form.cleaned_data.get('name')
        if name:
            form.instance.name = name.capitalize()

        ingredients = form.cleaned_data.get('ingredients')
        if ingredients:
            ingredients_list = [ingredient.strip().capitalize() for ingredient in ingredients.split(',')]
            form.instance.ingredients = ', '.join(ingredients_list)

        return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
  model = Recipe
  template_name = 'recipes/recipe_delete.html'

  def get_success_url(self):
    return ('/list/')
  
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes:list')  
    else:
        form = RecipeForm()
    
    context = {
        'form': form,
    }
    return render(request, 'recipes/add_recipe.html', context)

@login_required
def recipe_search(request):
    form = RecipeSearchForm(request.GET or None)
    recipes = Recipe.objects.all()

    # Filter recipes based on search criteria
    if form.is_valid():
        name = form.cleaned_data.get('name', '')
        difficulty = form.cleaned_data.get('difficulty', '')
        ingredient = form.cleaned_data.get('ingredient', '')

        if name:
            recipes = recipes.filter(name__icontains=name)
        if difficulty:
            recipes = recipes.filter(difficulty=difficulty)
        if ingredient:
            recipes = recipes.filter(ingredients__icontains=ingredient)
        

    # Convert QuerySet to pandas DataFrame
    recipe_df = pd.DataFrame.from_records(
       recipes.values('id', 'name', 'difficulty', 'cooking_time'))

    context = {
        'form': form,
        'recipe_df': recipe_df,
        'recipes': recipes,
    }
    return render(request, 'recipes/recipe_search.html', context)

@login_required
def recipe_analytics(request):
    # Fetch recipes from the database
    recipes = Recipe.objects.all()

    # Extract data
    recipe_names = [recipe.name for recipe in recipes]
    cooking_times = [recipe.cooking_time for recipe in recipes]
    difficulties = [recipe.difficulty for recipe in recipes]
    ingredient_counts = [len(recipe.ingredients.split(',')) for recipe in recipes]  

    # Create a dictionary for difficulties
    difficulty_counts = {difficulty: difficulties.count(difficulty) for difficulty in set(difficulties)}

    # Generate charts
    charts = generate_charts(recipe_names, cooking_times, difficulty_counts, ingredient_counts)

    return render(request, 'recipes/recipe_analytics.html', {'charts': charts})

@login_required
def about_page(request):
   return render(request, 'recipes/about.html')
