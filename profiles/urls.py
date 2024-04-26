from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('<int:pk>/update', views.ProfileUpdate.as_view(), name='profile_update'),
]
