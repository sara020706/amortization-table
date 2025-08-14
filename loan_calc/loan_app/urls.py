from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate/', views.loan_calculator, name='loan_calculator'),
]

