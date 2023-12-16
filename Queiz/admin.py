from django.contrib import admin
from .models import MCQAssignment, MCQQuestion, Option, CorrectAnswer,MCQSubmission

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4

class MCQQuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

class CorrectAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'option')

admin.site.register(MCQAssignment)
admin.site.register(MCQQuestion, MCQQuestionAdmin)
admin.site.register(CorrectAnswer, CorrectAnswerAdmin)
admin.site.register(MCQSubmission)
