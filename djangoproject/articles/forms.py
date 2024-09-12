from django import forms

# Create forms here
class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     # Validation conditions
    #     if title.lower().strip() == "the cleaned data":
    #         raise forms.ValidationError("This title is already taken")
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        # Validation conditions
        if title.lower().strip() == "the cleaned data":
            self.add_error('title', 'This title is taken') # Non field error
            # raise forms.ValidationError("This title is already taken")
        return cleaned_data