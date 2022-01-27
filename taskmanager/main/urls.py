
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('news', views.news),
    path('support', views.support),
    path('tours', views.tours),
    path('products', views.products),

]
