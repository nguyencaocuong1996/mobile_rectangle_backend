from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$', ListAllRestaurant.as_view()),
    url(r'^me/$', ListMyRestaurant.as_view()),
    url(r'^all/$', ListAllRestaurant.as_view()),
    url(r'^create/$', CreateRestaurant.as_view()),
]
