from django.contrib import admin
from .models import *

admin.site.register((Restaurant, Service, BookedRestaurant, FavoriteRestaurant))
