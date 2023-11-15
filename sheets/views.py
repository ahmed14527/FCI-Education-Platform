from rest_framework import viewsets
from .models import Sheet
from .serializers import  SheetSerializer
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.permissions import AllowAny

class SheetViewSet(viewsets.ModelViewSet):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer
    permission_classes = [AllowAny]

    
class SheetListAPIView(generics.ListAPIView):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer
    permission_classes = [AllowAny]
