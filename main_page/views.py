from typing import Any
from django.shortcuts import render
from django.views import generic
from categories import models as c_models

# Create your views here.

class MainPageView(generic.TemplateView):
    template_name = 'main_page/main-page.html'
    
    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(*args, **kwargs)

        context['categories'] = c_models.Category.objects.all()
        return context