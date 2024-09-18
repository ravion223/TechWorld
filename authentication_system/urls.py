from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('logout/', views.logout_view, name='log-out'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name='profile-detail')
]

app_name = 'authentication_system'