from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$', ListHotel.as_view()),
    url(r'^all/$', ListAllHotel.as_view()),
    url(r'^create/$', CreateHotel.as_view()),
]
