from django import forms
from .models import Recipe

class RecipeSearchForm(forms.Form): 
    DIFFICULTY_CHOICES = [
        ('', 'All'),
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Intermediate', 'Intermediate'),
        ('Hard', 'Hard'),
    ]

    name = forms.CharField(
        required=False,
        label="Recipe Name",
        widget=forms.TextInput(attrs={'placeholder': 'Enter recipe name'})
    )
    difficulty = forms.ChoiceField(
        required=False,
        choices=DIFFICULTY_CHOICES,
        label="Difficulty",
    )
    ingredient = forms.CharField(
        required=False,
        max_length=120,
        label='Ingredient',
        widget=forms.TextInput(attrs={'placeholder': 'Enter desired ingredient'})
    )

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'cooking_time', 'description', 'pic']
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 3}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter recipe description'}),
        }
        labels = {
            'pic': 'Recipe Image',
        }

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        if name:
            cleaned_data['name'] = name.capitalize()

        ingredients = cleaned_data.get('ingredients')
        if ingredients:
            ingredients_list = [ingredient.strip().capitalize() for ingredient in ingredients.split(',')]
            cleaned_data['ingredients'] = ', '.join(ingredients_list)

        return cleaned_data