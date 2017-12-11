from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', ListCustomer.as_view()),
    url(r'^create/$', CreateCustomer.as_view()),
    url(r'^login/', ObtainAuthToken.as_view())
]
