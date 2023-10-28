from django.contrib import admin
from .models import MCQAssignment, MCQQuestion, Option, MCQSubmission, MCQAnswer

admin.site.register(MCQAssignment)
admin.site.register(MCQQuestion)
admin.site.register(Option)
admin.site.register(MCQSubmission)
admin.site.register(MCQAnswer)