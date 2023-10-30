from django.urls import path
from rest_framework import routers
from .views import (
    MCQAssignmentViewSet,
    MCQAssignmentListAPIView,
    MCQQuestionViewSet,
    MCQQuestionListAPIView,
    OptionViewSet,
    OptionListAPIView,
    MCQSubmissionViewSet,
    MCQSubmissionListAPIView,
    MCQAnswerViewSet,
    MCQAnswerListAPIView,
)

router = routers.DefaultRouter()
router.register('create-mcq-assignments', MCQAssignmentViewSet)
router.register('create-mcq-questions', MCQQuestionViewSet)
router.register('create-options', OptionViewSet)
router.register('create-mcq-submissions', MCQSubmissionViewSet)
router.register('create-mcq-answers', MCQAnswerViewSet)

urlpatterns = [
    path('mcq-assignments/', MCQAssignmentListAPIView.as_view(), name='mcq-assignment-list'),
    path('mcq-questions/', MCQQuestionListAPIView.as_view(), name='mcq-question-list'),
    path('options/', OptionListAPIView.as_view(), name='option-list'),
    path('mcq-submissions/', MCQSubmissionListAPIView.as_view(), name='mcq-submission-list'),
    path('mcq-answers/', MCQAnswerListAPIView.as_view(), name='mcq-answer-list'),
]

urlpatterns += router.urls