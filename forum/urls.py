from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.TopicListView.as_view(), name='topic_list'),  # List of all topics
    path('topics/create/', views.TopicCreateView.as_view(), name='create_topic'), # Create a new topic
    path('<slug:slug>/', views.PostDetail.as_view(), name='thread'), # Details of individual post
    path('topics/<slug:slug>/', views.TopicDetailView.as_view(), name='topic_detail'),  # Detail view for a specific topic
    path('topics/<slug:topic_slug>/create/', views.PostCreate.as_view(), name='create_post'), # Create a new post in the topic
    path('posts/<slug:slug>/update/', views.PostUpdate.as_view(), name='update_post'), # Update a post
    path('posts/<slug:slug>/delete/', views.PostDelete.as_view(), name='delete_post'), # Delete a post
    path('post/<int:post_id>/comment/', views.add_comment_to_post, name='add_comment_to_post'), # Add a comment to a post
    path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'), # Edit a comment
    path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'), # Delete a comment
]
