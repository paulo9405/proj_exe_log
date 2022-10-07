from django.urls import path
from .views import home, functions_ex1, functions_ex6, functions_ex8


urlpatterns = [
    path('', home, name='home_functions'),
    path('functions_ex1', functions_ex1, name='functions_ex1_x'),
    path('functions_ex6', functions_ex6, name='functions_ex6_x'),
    path('functions_ex8', functions_ex8, name='functions_ex8_x'),
]