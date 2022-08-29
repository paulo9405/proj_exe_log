from django.urls import path

from .views import home, matrice_ex1, matrice_ex9


urlpatterns = [
    path('', home, name='home_matrices'),
    path('matrice_ex1', matrice_ex1, name='matrice_ex1_x'),
    path('matrice_ex9', matrice_ex9, name='matrice_ex9_x'),
]