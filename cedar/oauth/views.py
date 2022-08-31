from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone
from django.http import HttpRequest,HttpResponse
# Create your views here.

from .models import OauthUser

class OauthLogin(ListView):
    model = OauthUser
    # paginate_by = 100
    # template_name= ''

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
    # def get_queryset(self):
    #     return super().get_queryset()
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return HttpResponse(request.GET.get("username"))
