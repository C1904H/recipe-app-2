from django.db import models
from django.shortcuts import reverse

class Recipe(models.Model):
  name= models.CharField(max_length=50)
  ingredients= models.CharField(max_length=500, help_text="Separate each ingredient with comma")
  cooking_time= models.PositiveIntegerField(help_text="Cooking time in minutes")
  difficulty= models.CharField(max_length=20, editable=False, null=True, blank=True) 
  description= models.TextField()
  pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

  def calculate_difficulty(self):
    num_ingredients = len(self.ingredients.split(','))

    if self.cooking_time < 10 and num_ingredients <= 4:
        self.difficulty = 'Easy'
    elif self.cooking_time < 10 and num_ingredients >= 4:
        self.difficulty = 'Medium' 
    elif self.cooking_time >= 10 and num_ingredients < 4:
        self.difficulty = 'Intermediate'
    else:
        self.difficulty = 'Hard'

  def save(self, *args, **kwargs):
        self.calculate_difficulty()
        super().save(*args, **kwargs)

  def __str__(self):
    return str(self.name)

  def get_absolute_url(self):
    return reverse ('recipes:detail', kwargs={'pk': self.pk})
