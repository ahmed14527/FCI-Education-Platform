from django.urls import path
from .views import CommentCreateView, CommentListAPIView

urlpatterns = [
    path('collaborate/create/', CommentCreateView.as_view(), name='collaborate_create'),
    path('collaborations/', CommentListAPIView.as_view(), name='collaborations_list'),
]