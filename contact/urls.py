from django.urls import path
from .views import contactar

urlpatterns = [ path('', contactar, name='contact')]  