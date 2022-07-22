from django.urls import path

from .views import home, ex1, ex2, ex3, ex4, ex5

urlpatterns = [
    path('', home, name='home'),
    path('ex1', ex1, name='ex1_x'),
    path('ex2', ex2, name='ex2_x'),
    path('ex3', ex3, name='ex3_x'),
    path('ex4', ex4, name='ex4_x'),
    path('ex5', ex5, name='ex5_x'),

]