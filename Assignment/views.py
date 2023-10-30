from rest_framework import viewsets
from .models import  MCQAssignment, MCQQuestion, Option, MCQSubmission, MCQAnswer
from .serializers import  MCQAssignmentSerializer, MCQQuestionSerializer, OptionSerializer, MCQSubmissionSerializer, MCQAnswerSerializer
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics


class MCQAssignmentViewSet(viewsets.ModelViewSet):
    queryset = MCQAssignment.objects.all()
    serializer_class = MCQAssignmentSerializer
    permission_classes = [IsAdminUser]

    
@method_decorator(login_required, name='dispatch')
class MCQAssignmentListAPIView(generics.ListAPIView):
    queryset = MCQAssignment.objects.all()
    serializer_class = MCQAssignmentSerializer

class MCQQuestionViewSet(viewsets.ModelViewSet):
    queryset = MCQQuestion.objects.all()
    serializer_class = MCQQuestionSerializer
    permission_classes = [IsAdminUser]

    
@method_decorator(login_required, name='dispatch')
class MCQQuestionListAPIView(generics.ListAPIView):
    queryset = MCQQuestion.objects.all()
    serializer_class = MCQQuestionSerializer
    
    
class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAdminUser]


@method_decorator(login_required, name='dispatch')
class OptionListAPIView(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class MCQSubmissionViewSet(viewsets.ModelViewSet):
    queryset = MCQSubmission.objects.all()
    serializer_class = MCQSubmissionSerializer
    permission_classes = [IsAdminUser]

    
@method_decorator(login_required, name='dispatch')
class MCQSubmissionListAPIView(generics.ListAPIView):
    queryset = MCQSubmission.objects.all()
    serializer_class = MCQSubmissionSerializer

class MCQAnswerViewSet(viewsets.ModelViewSet):
    queryset = MCQAnswer.objects.all()
    serializer_class = MCQAnswerSerializer
    permission_classes = [IsAdminUser]

@method_decorator(login_required, name='dispatch')
class MCQAnswerListAPIView(generics.ListAPIView):
    queryset = MCQAnswer.objects.all()
    serializer_class = MCQAnswerSerializer
