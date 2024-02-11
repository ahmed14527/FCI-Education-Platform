from django.urls import path
from .views import CreateCommentViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'collaborate', CreateCommentViewSet)
urlpatterns = [
    #path('collaborate/create/', CommentCreateView.as_view(), name='collaborate_create'),
    #path('collaborations/', CommentListAPIView.as_view(), name='collaborations_list'),
]+router.urls