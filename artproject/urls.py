from django.contrib import admin
from django.urls import path, include
from artspot.views import (landing_page, home, about)
from django.conf.urls.static import static

app_name = 'artspot'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artspot/', include('artspot.urls')), 
    path('about/', about, name='about'),
    path('', home, name='home')
]

