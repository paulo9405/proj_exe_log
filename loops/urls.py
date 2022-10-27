from django.urls import path
from .views import home, loops_ex22


urlpatterns = [
    path('', home, name='home_loops'),
    path('loops_ex22', loops_ex22, name='loops_ex22_x'),

]