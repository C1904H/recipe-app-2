# Generated by Django 5.1.5 on 2025-01-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='https://res.cloudinary.com/dh7gymjoq/image/upload/v12345678/no_picture.jpg', upload_to='recipes'),
        ),
    ]
