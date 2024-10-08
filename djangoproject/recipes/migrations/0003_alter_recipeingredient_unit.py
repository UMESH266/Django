# Generated by Django 3.2.25 on 2024-09-14 02:32

from django.db import migrations, models
import recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_recipeingredients_recipeingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=50, validators=[recipes.validators.validate_unit_of_measurement]),
        ),
    ]
