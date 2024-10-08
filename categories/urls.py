from django.urls import path
from . import views

urlpatterns = [
    path('category/create/', views.CategoryCreateView.as_view(), name='create-category'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:category_id>/delete/', views.delete_category, name='category-delete'),
    path('category/<int:category_id>/add/product/', views.ProductCreateView.as_view(), name='add-product'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:product_id>/delete/', views.delete_product, name='product-delete')
]

app_name = 'categories'