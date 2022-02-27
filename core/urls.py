from django.urls import path
from .views import home, about, blog, contact, sample, store


urlpatterns = [
    path('', home , name='home'),
    path('about/', about , name='about'),
    path('blog/', blog , name='blog'),
    path('contact/', contact , name='contact'),
    path('sample/', sample , name='sample'),
    path('store/', store , name='store'),

]