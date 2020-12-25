from django.urls import path
from blogging.views import list_view, detail_view, create_post
from blogging.feeds import LatestEntriesFeed

urlpatterns = [
    path('', list_view, name='blog_index'),
    path('posts/<int:post_id>/', detail_view, name='blog_detail'),
    path('create/', create_post, name='create_post'),
    path('latest/feed/', LatestEntriesFeed()),
]
