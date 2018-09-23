from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$', ListServiceView.as_view()),
    url(r'^categories/$', ListCategoryView.as_view()),
]
