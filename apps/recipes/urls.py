from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, recipe_search, recipe_analytics, add_recipe, RecipeUpdateView, RecipeDeleteView, about_page

app_name = 'recipes'

urlpatterns = [
  path('', home, name='home'),
  path('list/', RecipeListView.as_view(), name='list'),
  path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
  path('search/', recipe_search, name='search'),
  path('analytics/', recipe_analytics, name='analytics'),
  path('add/', add_recipe, name='add'),
  path('update/<pk>', RecipeUpdateView.as_view(), name='update'),
  path('delete/<pk>', RecipeDeleteView.as_view(), name='delete'),
  path('about', about_page, name='about'),
]