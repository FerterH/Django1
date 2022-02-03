
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about, name='info'),
    path('news', views.news, name='news'),
    path('support', views.support, name='support'),
    path('tours', views.tours, name='tours'),
    path('products', views.products, name='products'),
    path('maybe', views.maybe),
    path('empty', views.empty, name='vzlom'),

]
