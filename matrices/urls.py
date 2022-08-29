from django.urls import path

from .views import home, matrice_ex1, matrice_ex8


urlpatterns = [
    path('', home, name='home_matrices'),
    path('matrice_ex1', matrice_ex1, name='matrice_ex1_x'),
    path('matrice_ex8', matrice_ex8, name='matrice_ex8_x'),
]