from django.urls import include, path
from rest_framework import routers
from Assignment.views import  MCQAssignmentViewSet, MCQQuestionViewSet, OptionViewSet, MCQSubmissionViewSet, MCQAnswerViewSet

router = routers.DefaultRouter()
router.register(r'assignments', MCQAssignmentViewSet)
router.register(r'questions', MCQQuestionViewSet)
router.register(r'options', OptionViewSet)
router.register(r'submissions', MCQSubmissionViewSet)
router.register(r'answers', MCQAnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]