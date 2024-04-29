from rest_framework import viewsets
from .models import ML
from ml.serilaizers import  MLSerializer
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.permissions import AllowAny

class MLViewSet(viewsets.ModelViewSet):
    queryset = ML.objects.all()
    serializer_class = MLSerializer
    permission_classes = [AllowAny]

    
class MLListAPIView(generics.ListAPIView):
    queryset = ML.objects.all()
    serializer_class = MLSerializer
    permission_classes = [AllowAny]
