
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('', include('ecourse_admin.urls')),
     path('', include('api.urls')),
    path('sqlite/', admin.site.urls)
]
