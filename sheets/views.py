from rest_framework import viewsets
from .models import Sheets
from .serializers import  SheetsSerializer
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.permissions import AllowAny

class SheetsViewSet(viewsets.ModelViewSet):
    queryset = Sheets.objects.all()
    serializer_class = SheetsSerializer
    permission_classes = [AllowAny]

    
class SheetsListAPIView(generics.ListAPIView):
    queryset = Sheets.objects.all()
    serializer_class = SheetsSerializer
    permission_classes = [AllowAny]
