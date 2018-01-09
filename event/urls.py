from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', ListAllEvent.as_view()),
    url(r'^all/$', ListAllEvent.as_view()),
]
