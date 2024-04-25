from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.PostList.as_view(), name='forum'),
    path('new/', login_required(views.PostCreate.as_view()), name='new_thread'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='thread'),
    path('<slug:slug>/update/', login_required(views.PostUpdate.as_view()), name='update_thread'),
    path('<slug:slug>/delete/', login_required(views.PostDelete.as_view()), name='delete_thread'),
    path('<slug:slug>/comment/', login_required(views.CommentCreate.as_view()), name='comment'),
    path('<slug:slug>/comment/<int:pk>/update/', login_required(views.CommentUpdate.as_view()), name='update_comment'),
    path('<slug:slug>/comment/<int:pk>/delete/', login_required(views.CommentDelete.as_view()), name='delete_comment'),
]
