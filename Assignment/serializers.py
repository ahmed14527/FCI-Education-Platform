from rest_framework import serializers
from .models import  MCQAssignment, MCQQuestion, Option, MCQSubmission, MCQAnswer



class MCQAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQAssignment
        fields = '__all__'

class MCQQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQQuestion
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class MCQSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQSubmission
        fields = '__all__'

class MCQAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQAnswer
        fields = '__all__'