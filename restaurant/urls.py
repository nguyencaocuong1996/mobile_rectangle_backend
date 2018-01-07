from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$', ListAllRestaurant.as_view()),
    url(r'^me/$', ListMyRestaurant.as_view()),
    url(r'^all/$', ListAllRestaurant.as_view()),
    url(r'^create/$', CreateRestaurant.as_view()),
    url(r'^favorites/$', ListFavoriteRestaurant.as_view()),
    url(r'^add-favorite/$', AddFavorite.as_view()),
    url(r'^list-booked/$', ListBookedRestaurant.as_view()),
    url(r'^book/$', BookRestaurant.as_view()),
]
