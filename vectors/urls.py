from django.urls import path
from .views import home, ex1, ex4

urlpatterns = [
    path('', home, name='home'),
    path('ex1', ex1, name='ex1_x'),
    path('ex4', ex4, name='ex4_x'),

]