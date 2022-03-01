from django.urls import path
from .views import blog, category

urlpatterns = [
    path('', blog, name='blog'),
    ## int: transforma el string category_id de la path a entero
    path('category/<int:category_id>/', category, name='category'),
]