
from django.contrib import admin
from django.urls import include,path
from . import views;
urlpatterns = [
    path('admin/login', views.index , name="login"),
    path('admin/dashboard', views.dashboard , name="dashboard"),
    path('admin/addcourse/<str:mode>', views.addcourse , name="addcourse"),
    path('admin/uploadvideos/<str:id>', views.uploadvideos , name="profile"),
    path('admin/profile', views.profile , name="profile"),
    path('admin/settings', views.settings , name="settings"),
    path('admin/logout', views.logout , name="logout"),
]
