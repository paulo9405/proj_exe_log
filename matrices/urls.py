from django.urls import path

from .views import home, matrice_ex1, matrice_ex5


urlpatterns = [
    path('', home, name='home_matrices'),
    path('matrice_ex1', matrice_ex1, name='matrice_ex1_x'),
    path('matrice_ex5', matrice_ex5, name='matrice_ex5_x'),
]