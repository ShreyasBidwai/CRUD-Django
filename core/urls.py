from django.contrib import admin
from django.urls import path
from home.views import *
from veggie.views import *
urlpatterns = [
    path('recipe', recipe),
    path('', home),
    path('admin/', admin.site.urls),
]
