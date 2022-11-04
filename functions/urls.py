from django.urls import path
from .views import (
    home,
    functions_ex1,
    functions_ex2,
    functions_ex3,
    functions_ex6,
    functions_ex7,
    functions_ex8,
    functions_ex11

)


urlpatterns = [
    path('', home, name='home_functions'),
    path('functions_ex1', functions_ex1, name='functions_ex1_x'),
    path('functions_ex2', functions_ex2, name='functions_ex2_x'),
    path('functions_ex3', functions_ex3, name='functions_ex3_x'),
    path('functions_ex6', functions_ex6, name='functions_ex6_x'),
    path('functions_ex7', functions_ex7, name='functions_ex7_x'),
    path('functions_ex8', functions_ex8, name='functions_ex8_x'),
    path('functions_ex11', functions_ex11, name='functions_ex11_x'),
]