from rest_framework import viewsets
from .models import Sheet
from .serializers import  SheetSerializer
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics

@method_decorator(login_required, name='dispatch')
class SheetViewSet(viewsets.ModelViewSet):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer
    
    
class SheetListAPIView(generics.ListAPIView):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer
    permission_classes = [IsAdminUser]
