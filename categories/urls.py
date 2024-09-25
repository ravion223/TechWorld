from django.urls import path
from . import views

urlpatterns = [
    path('category/create/', views.CategoryCreateView.as_view(), name='create-category'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/<int:category_id>/add/product/', views.ProductCreateView.as_view(), name='add-product')
]

app_name = 'categories'