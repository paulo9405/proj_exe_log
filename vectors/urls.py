from django.urls import path

from .views import (
    home, ex1, ex2,
    ex3, ex4, ex5,
    ex6, ex7, ex9,
    ex10, ex11, ex12,
    ex13
)

urlpatterns = [
    path('', home, name='home'),
    path('ex1', ex1, name='ex1_x'),
    path('ex2', ex2, name='ex2_x'),
    path('ex3', ex3, name='ex3_x'),
    path('ex4', ex4, name='ex4_x'),
    path('ex5', ex5, name='ex5_x'),
    path('ex6', ex6, name='ex6_x'),
    path('ex7', ex7, name='ex7_x'),
    path('ex9', ex9, name='ex9_x'),
    path('ex10', ex10, name='ex10_x'),
    path('ex11', ex11, name='ex11_x'),
    path('ex12', ex12, name='ex12_x'),
    path('ex13', ex13, name='ex13_x'),

]