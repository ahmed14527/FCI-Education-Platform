from rest_framework import viewsets
from .models import Sheet
from .serializers import  SheetSerializer


class SheetViewSet(viewsets.ModelViewSet):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer