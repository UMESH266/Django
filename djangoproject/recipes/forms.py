from dataclasses import fields
from logging import PlaceHolder
from django import forms
from .models import Recipe, RecipeIngredient

class RecipeForm(forms.ModelForm):
    error_css_class = "error-field"
    required_css_class = "required-field"
    # Help text to name widget
    name = forms.CharField(help_text='This is your help! <a href="/contact">Contact us</a>')

    # Refere documentation for built in widgets
    # name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Recipe name"}))
    # description = forms.CharField(widget=forms.Textarea(attrs={"rows":3}))
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "placeholder":f"Recipe {field}",
                "class": "form-control"
            }
            self.fields[str(field)].widget.attrs.update(new_data)

        # self.fields['name'].label = ''
        # self.fields['name'].widget.attrs.update({'class':"form-control-2"})

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['name', 'quantity', 'unit'] 
