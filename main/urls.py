from . import views
from django.urls import path

app_name='main'
urlpatterns = [path('', views.main, name='main')]