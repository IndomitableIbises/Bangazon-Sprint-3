from django import forms
from website.models import Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('cat_name',)