from django.contrib import admin
from .models import Questions, Options, CustomerFeedback, CustomerResponse

class QuestionInline(admin.TabularInline):
    model = CustomerFeedback.question.through
    extra = 1

class CustomerFeedbackAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Questions)
admin.site.register(Options)
admin.site.register(CustomerFeedback, CustomerFeedbackAdmin)
admin.site.register(CustomerResponse)