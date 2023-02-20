from django.urls import path
from .views import PostDetail ,PostList , CommentCreate , VoteCreate

urlpatterns = [
    path('' , PostList.as_view() , name = 'post_list'),
    path('<int:pk>/' , PostDetail.as_view() , name='post_detail'),
    path('<int:pk>/comments/', CommentCreate.as_view(), name='comment_create'),
    path('<int:pk>/votes/', VoteCreate.as_view(), name='vote_create'),
]
