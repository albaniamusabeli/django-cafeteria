from django.urls import path
from .views import page

urlpatterns = [
    ## int: transforma el string page_id de la path a entero
    path('<int:page_id>/', page, name='page'),
]