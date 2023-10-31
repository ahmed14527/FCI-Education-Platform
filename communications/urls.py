from django.urls import path
from .views import CommentCreateView, CommentListAPIView

urlpatterns = [
    path('comments/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/', CommentListAPIView.as_view(), name='comment_list'),
]