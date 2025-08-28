from django.contrib import admin
from django.urls import path
from veggie.views import *
urlpatterns = [
    path('', recipe),
    path('admin/', admin.site.urls),
]
