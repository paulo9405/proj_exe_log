from django.urls import path
from .views import home, functions_ex1, functions_ex2


urlpatterns = [
    path('', home, name='home_functions'),
    path('functions_ex1', functions_ex1, name='functions_ex1_x'),
    path('functions_ex2', functions_ex2, name='functions_ex2_x'),
]