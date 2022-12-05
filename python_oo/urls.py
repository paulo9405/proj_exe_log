from django.urls import path
from .views import home, python_oo_ex1, python_oo_ex9

urlpatterns = [
    path('', home, name='home_python_oo'),
    path('python_oo_ex1', python_oo_ex1, name='python_oo_ex1_x'),
    path('python_oo_ex9', python_oo_ex9, name='python_oo_ex9_x'),
]