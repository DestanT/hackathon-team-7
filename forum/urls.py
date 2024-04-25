from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.TopicListView.as_view(), name='topic_list'),  # List of all topics
    path('topics/<slug:slug>/', views.TopicDetailView.as_view(), name='topic_detail'),  # Detail view for a specific topic
    path('posts/', views.PostList.as_view(), name='forum'),  # List all posts
    path('new/', login_required(views.PostCreate.as_view()), name='new_thread'),  # Create a new post
    path('<slug:slug>/', views.PostDetail.as_view(), name='thread'),  # Detail view for a specific post
    path('<slug:slug>/update/', login_required(views.PostUpdate.as_view()), name='update_thread'),  # Update a specific post
    path('<slug:slug>/delete/', login_required(views.PostDelete.as_view()), name='delete_thread'),  # Delete a specific post
    path('<slug:slug>/comment/', login_required(views.CommentCreate.as_view()), name='comment'),  # Add a comment to a post
    path('<slug:slug>/comment/<int:pk>/update/', login_required(views.CommentUpdate.as_view()), name='update_comment'),  # Update a comment
    path('<slug:slug>/comment/<int:pk>/delete/', login_required(views.CommentDelete.as_view()), name='delete_comment'),  # Delete a comment
]
