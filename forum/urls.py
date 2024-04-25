from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.TopicListView.as_view(), name='topic_list'),  # List of all topics
    path('topics/create/', views.TopicCreateView.as_view(), name='create_topic'), # Create a new topic
    path('topics/<slug:slug>/', views.TopicDetailView.as_view(), name='topic_detail'),  # Detail view for a specific topic
    path('posts/', views.PostList.as_view(), name='forum'),  # List all posts
    path('<slug:slug>/', views.PostDetail.as_view(), name='thread'),
    path('topics/<slug:topic_slug>/create/', views.PostCreate.as_view(), name='create_post'), # Create a new post in the topic
]
