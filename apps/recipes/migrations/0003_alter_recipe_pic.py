# Generated by Django 5.1.5 on 2025-01-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='recipes/no_picture.jpg', upload_to='recipes'),
        ),
    ]
