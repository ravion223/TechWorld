from django import forms
from . import models


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ('name',)
        labels = [
            ('name', 'Name')
        ]