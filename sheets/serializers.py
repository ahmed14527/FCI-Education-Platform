from rest_framework import serializers
from .models import Sheets




class SheetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheets
        fields = '__all__'