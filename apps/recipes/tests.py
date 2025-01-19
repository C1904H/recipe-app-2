from django.test import TestCase
from .models import Recipe
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RecipeForm, RecipeSearchForm

class RecipeModelTest(TestCase):

  def setUpTestData():
    Recipe.objects.create(
      name='Cheesy Toast', 
      ingredients='Bread, Cheese, Pickles',
      cooking_time=5,
      description='Fast comfort food!'
    )

  def test_recipe_name(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')
    
  def test_recipe_name_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('name').max_length
    self.assertEqual(max_length, 50)

  def test_recipe_str_method(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(str(recipe), 'Cheesy Toast')

  def test_recipe_creation(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(recipe.name, 'Cheesy Toast')
    self.assertEqual(recipe.cooking_time, 5)
    self.assertIn('Bread', recipe.ingredients)

  def test_calculate_difficulty(self):
    recipe = Recipe.objects.get(id=1)
    recipe.cooking_time = 15
    recipe.ingredients = 'Ingredient1, Ingredient2'
    recipe.save()
    self.assertEqual(recipe.difficulty, 'Intermediate')

  def test_get_absolute_url(self):
       recipe = Recipe.objects.get(id=1)
       self.assertEqual(recipe.get_absolute_url(), '/list/1')
  

class RecipeFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'name': 'Pasta',
            'ingredients': 'Tomatoes, Pasta, Cheese',
            'cooking_time': 20,
            'description': 'Simple pasta recipe',
        }
        form = RecipeForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'name': '',  
            'ingredients': 'Tomatoes, Pasta',
            'cooking_time': -5,  
            'description': 'A quick meal',
        }
        form = RecipeForm(data)
        self.assertFalse(form.is_valid())

    def test_ingredient_formatting(self):
        data = {
            'name': 'toast',
            'ingredients': 'bread, cheese',
            'cooking_time': 10,
            'description': 'A quick snack',
        }
        form = RecipeForm(data)
        if form.is_valid():
            recipe = form.save(commit=False)
            self.assertEqual(recipe.name, 'Toast')
            self.assertEqual(recipe.ingredients, 'Bread, Cheese')


class RecipeSearchFormTest(TestCase):
    def test_valid_form(self):
        data = {'name': 'Pasta', 'difficulty': 'Easy', 'ingredient': 'Tomatoes'}
        form = RecipeSearchForm(data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        data = {}
        form = RecipeSearchForm(data)
        self.assertTrue(form.is_valid())  

    def test_max_length_validation(self):
        data = {'ingredient': 'a' * 121} 
        form = RecipeSearchForm(data)
        self.assertFalse(form.is_valid())


class RecipeViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        Recipe.objects.create(
            name='Recipe1',
            ingredients='Ingredient1, Ingredient2',
            cooking_time=10,
            description='Test description'
        )

    def test_recipe_list_view_requires_login(self):
        response = self.client.get(reverse('recipes:list'))
        self.assertRedirects(response, '/login/?next=/list/')

    def test_recipe_list_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('recipes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Recipe1')

    def test_recipe_detail_view_requires_login(self):
        recipe = Recipe.objects.get(name='Recipe1')
        response = self.client.get(reverse('recipes:detail', args=[recipe.id]))
        self.assertRedirects(response, f'/login/?next=/list/{recipe.id}')

    def test_recipe_detail_view(self):
        self.client.login(username='testuser', password='12345')
        recipe = Recipe.objects.get(name='Recipe1')
        response = self.client.get(reverse('recipes:detail', args=[recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test description')

    def test_add_recipe_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(
            reverse('recipes:add'),
            {
                'name': 'New Recipe',
                'ingredients': 'Tomato, Basil',
                'cooking_time': 15,
                'description': 'Tasty and simple',
            }
        )
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Recipe.objects.filter(name='New recipe').exists())

    def test_update_recipe_view(self):
        self.client.login(username='testuser', password='12345')
        recipe = Recipe.objects.get(name='Recipe1')
        response = self.client.post(
            reverse('recipes:update', args=[recipe.id]),
            {
                'name': 'Updated Recipe',
                'ingredients': 'Updated Ingredient',
                'cooking_time': 20,
                'description': 'Updated description',
            }
        )
        recipe.refresh_from_db()
        self.assertEqual(recipe.name, 'Updated recipe')
        self.assertEqual(response.status_code, 302)

    def test_delete_recipe_view(self):
        self.client.login(username='testuser', password='12345')
        recipe = Recipe.objects.get(name='Recipe1')
        response = self.client.post(reverse('recipes:delete', args=[recipe.id]))
        self.assertFalse(Recipe.objects.filter(id=recipe.id).exists())
        self.assertEqual(response.status_code, 302)  
