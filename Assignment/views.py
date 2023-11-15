from rest_framework import viewsets
from .models import  MCQAssignment, MCQQuestion, Option, MCQSubmission, MCQAnswer
from .serializers import  MCQAssignmentSerializer, MCQQuestionSerializer, OptionSerializer, MCQSubmissionSerializer, MCQAnswerSerializer
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.permissions import AllowAny


class MCQAssignmentViewSet(viewsets.ModelViewSet):
    queryset = MCQAssignment.objects.all()
    serializer_class = MCQAssignmentSerializer
    permission_classes = [AllowAny]

    
class MCQAssignmentListAPIView(generics.ListAPIView):
    queryset = MCQAssignment.objects.all()
    serializer_class = MCQAssignmentSerializer
    permission_classes = [AllowAny]

class MCQQuestionViewSet(viewsets.ModelViewSet):
    queryset = MCQQuestion.objects.all()
    serializer_class = MCQQuestionSerializer
    permission_classes = [AllowAny]

    
class MCQQuestionListAPIView(generics.ListAPIView):
    queryset = MCQQuestion.objects.all()
    serializer_class = MCQQuestionSerializer
    permission_classes = [AllowAny]

    
class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [AllowAny]


class OptionListAPIView(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [AllowAny]

class MCQSubmissionViewSet(viewsets.ModelViewSet):
    queryset = MCQSubmission.objects.all()
    serializer_class = MCQSubmissionSerializer
    permission_classes = [AllowAny]

    
class MCQSubmissionListAPIView(generics.ListAPIView):
    queryset = MCQSubmission.objects.all()
    serializer_class = MCQSubmissionSerializer
    permission_classes = [AllowAny]

class MCQAnswerViewSet(viewsets.ModelViewSet):
    queryset = MCQAnswer.objects.all()
    serializer_class = MCQAnswerSerializer
    permission_classes = [AllowAny]

class MCQAnswerListAPIView(generics.ListAPIView):
    queryset = MCQAnswer.objects.all()
    serializer_class = MCQAnswerSerializer
    permission_classes = [AllowAny]
