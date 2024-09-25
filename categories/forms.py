from django import forms
from . import models


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ('name',)
        labels = [
            ('name', 'Name')
        ]


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ('name', 'description', 'price', 'product_image')
        labels = [
            ('name', 'Name'),
            ('description', 'Description'),
            ('price', 'Price')
        ]