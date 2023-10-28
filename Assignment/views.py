from rest_framework import viewsets
from .models import  MCQAssignment, MCQQuestion, Option, MCQSubmission, MCQAnswer
from .serializers import  MCQAssignmentSerializer, MCQQuestionSerializer, OptionSerializer, MCQSubmissionSerializer, MCQAnswerSerializer



class MCQAssignmentViewSet(viewsets.ModelViewSet):
    queryset = MCQAssignment.objects.all()
    serializer_class = MCQAssignmentSerializer

class MCQQuestionViewSet(viewsets.ModelViewSet):
    queryset = MCQQuestion.objects.all()
    serializer_class = MCQQuestionSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class MCQSubmissionViewSet(viewsets.ModelViewSet):
    queryset = MCQSubmission.objects.all()
    serializer_class = MCQSubmissionSerializer

class MCQAnswerViewSet(viewsets.ModelViewSet):
    queryset = MCQAnswer.objects.all()
    serializer_class = MCQAnswerSerializer