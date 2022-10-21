from django.urls import path
from .views import (
    home,
    loops_ex1,
)


urlpatterns = [
    path('', home, name='home_loops'),
    path('loops_ex1', loops_ex1, name='loops_ex1_x'),
]