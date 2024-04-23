from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileList.as_view(), name='profile_list'),
]
