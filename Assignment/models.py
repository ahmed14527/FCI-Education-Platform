from django.db import models
from django.contrib.auth.models import User

class MCQAssignment(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.title)
    

class MCQQuestion(models.Model):
    Question = models.TextField()
    assignment = models.ForeignKey(MCQAssignment, on_delete=models.CASCADE, related_name='questions')
    def __str__(self):
        return self.Question
    
    
class Option(models.Model):
    Option = models.CharField(max_length=100)
    question = models.ForeignKey(MCQQuestion, on_delete=models.CASCADE, related_name='options')
    def __str__(self):
        return self.Option
    
    
class MCQSubmission(models.Model):
    Submission = models.ForeignKey(MCQAssignment, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments')
    
    def __str__(self):
        return f"MCQSubmission - User: {self.user}"
    
class MCQAnswer(models.Model):
    question = models.ForeignKey(MCQQuestion, on_delete=models.CASCADE, related_name='answers')
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"MCQAnswer - Selected Option: {self.selected_option}"
    
    
    
    