from django.urls import path
from .views import home, loops_ex7


urlpatterns = [
    path('', home, name='home_loops'),
    path('loops_ex7', loops_ex7, name='loops_ex7_x'),

]