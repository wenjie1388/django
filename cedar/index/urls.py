
from unicodedata import name
from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path(
        r'',
        views.IndexViews.as_view(),
        name = 'index'
    ),

]