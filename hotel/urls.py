from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$', ListHotel.as_view()),
    url(r'^me/$', ListMyHotel.as_view()),
    url(r'^all/$', ListAllHotel.as_view()),
    url(r'^create/$', CreateHotel.as_view()),
    url(r'^favorites/$', ListFavoriteHotel.as_view()),
    url(r'^add-favorite/$', AddFavorite.as_view()),
    url(r'^list-booked/$', ListBookedHotel.as_view()),
    url(r'^book/$', BookHotel.as_view()),
]
