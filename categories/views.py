from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from . import models
from . import forms

# Create your views here.

def is_user_admin_or_moderator(user):
    return user.is_authenticated and (user.access == 'moder' or user.is_staff)


@method_decorator(user_passes_test(is_user_admin_or_moderator), name='dispatch')
class CategoryCreateView(generic.CreateView):
    model = models.Category
    form_class = forms.CreateCategoryForm
    template_name = 'categories/category-create.html'
    success_url = reverse_lazy('main_page:main-page')