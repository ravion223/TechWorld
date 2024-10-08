from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
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


class CategoryDetailView(generic.DetailView):
    model = models.Category
    template_name = 'categories/category-detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['products'] = context['category'].products.all()

        return context
    

@method_decorator(user_passes_test(is_user_admin_or_moderator), name='dispatch')
class CategoryUpdateView(generic.UpdateView):
    model = models.Category
    template_name = 'categories/category-update.html'
    form_class = forms.CategoryUpdateForm
    success_url = reverse_lazy('main_page:main-page')


user_passes_test(is_user_admin_or_moderator)
def delete_category(request, category_id):
    if request.method == 'POST':
        category = get_object_or_404(models.Category, id=category_id)
        category.delete()
        return JsonResponse({'message': 'Category deleted successfully'}) and  redirect('main_page:main-page')
    else:
        return JsonResponse({'error': 'Invalid request method'})
    

@method_decorator(user_passes_test(is_user_admin_or_moderator), name='dispatch')
class ProductCreateView(generic.CreateView):
    model = models.Product
    form_class = forms.CreateProductForm
    template_name = 'categories/create-product.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        
        if category_id:
            context['category_id']= category_id
        else:
            raise ValueError('Category with that id is not found')
        
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product = form.save(commit=False)
        category_id = self.kwargs.get('category_id')

        try:
            category = models.Category.objects.get(id=category_id)
        except models.Category.DoesNotExist:
            raise ValueError("Invalid category ID")
        
        product.category = category
        
        product.save()

        return super().form_valid(form)
    
    def get_success_url(self, *args, **kwargs) -> str:
        return reverse_lazy('categories:category-detail', kwargs={'pk': self.kwargs.get('category_id')})
    

class ProductDetailView(generic.DetailView):
    model = models.Product
    template_name = 'categories/product-detail.html'
    context_object_name = 'product'


@method_decorator(user_passes_test(is_user_admin_or_moderator), name='dispatch')
class ProductUpdateView(generic.UpdateView):
    model = models.Product
    template_name = 'categories/product-update.html'
    form_class = forms.UpdateProductForm
    
    def get_success_url(self) -> str:
        return reverse_lazy('categories:product-detail', kwargs={'pk': self.kwargs.get('pk')})
    

user_passes_test(is_user_admin_or_moderator)
def delete_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(models.Product, id=product_id)
        category_id = product.category.id
        product.delete()
        return redirect(reverse('categories:category-detail', args=[category_id]))
    else:
        return JsonResponse({'error': 'Invalid request method'})