from django.urls import path
from .views import(
    home,
    matrice_ex1,
    matrice_ex2,
    matrice_ex3,
    matrice_ex4,
    matrice_ex5,
    matrice_ex6,
    matrice_ex7,
)



urlpatterns = [
    path('', home, name='home_matrices'),
    path('matrice_ex1', matrice_ex1, name='matrice_ex1_x'),
    path('matrice_ex2', matrice_ex2, name='matrice_ex2_x'),
    path('matrice_ex3', matrice_ex3, name='matrice_ex3_x'),
    path('matrice_ex4', matrice_ex4, name='matrice_ex4_x'),
    path('matrice_ex5', matrice_ex5, name='matrice_ex5_x'),
    path('matrice_ex6', matrice_ex6, name='matrice_ex6_x'),
    path('matrice_ex7', matrice_ex7, name='matrice_ex7_x'),
]