from django.urls import path

from .views import home, matrice_ex1, matrice_ex4


urlpatterns = [
    path('', home, name='home_matrices'),
    path('matrice_ex1', matrice_ex1, name='matrice_ex1_x'),
    path('matrice_ex4', matrice_ex4, name='matrice_ex4_x'),
]