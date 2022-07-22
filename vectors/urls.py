from django.urls import path
from .views import home, ex1, ex2

urlpatterns = [
    path('', home, name='home'),
    path('ex1', ex1, name='ex1_x'),
    path('ex5', ex2, name='ex2_x'),

]