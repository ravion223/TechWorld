from django import forms
from . import models


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ('name',)
        labels = [
            ('name', 'Name')
        ]


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ('name',)
        labels = [
            ('name', '')
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


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ('name', 'product_image', 'description', 'price')


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ('content', 'rate')
        labels = {
            'content': 'Commentary'
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type here...'}),
            'rate': forms.NumberInput(attrs={'class': 'form-range', 'type': 'range', 'min': '1', 'max': '5', 'step': '1'})
        }