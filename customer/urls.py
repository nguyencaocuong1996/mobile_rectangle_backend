from django.conf.urls import url, include
from .views import *
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^$', ListCustomer.as_view()),
    url(r'^create/$', CreateCustomer.as_view()),
    url(r'^login/', views.obtain_auth_token)
]
