from django.contrib import admin
from .models import *

admin.site.register((Hotel, Service, FavoriteHotel, BookedHotel))
