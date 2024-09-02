from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main-page')
]

app_name = 'main_page'