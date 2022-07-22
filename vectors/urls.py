from django.urls import path
from .views import home, ex1

urlpatterns = [
    path('', home, name='home'),
    path('ex1', ex1, name='ex1_x'),

]