from django.urls import path
from . import views
app_name = 'AIMDApp'

urlpatterns = [
    path('',views.Home, name = 'Home')
]