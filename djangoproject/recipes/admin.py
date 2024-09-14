from django.contrib import admin
from .models import RecipeIngredient, Recipe
from django.contrib.auth import get_user_model

# Register your models here.

User = get_user_model()

# admin.site.register(RecipeIngredient)

# class RecipeIngredientInline(admin.TabularInline):
#     model = RecipeIngredient
#     extra = 1
#     fields = ['name', 'quantity', 'unit', 'direction']

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    # fields = ['name', 'quantity', 'unit', 'direction']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)