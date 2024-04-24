from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='forum'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='thread'),
]