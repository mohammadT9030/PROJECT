from django.contrib import admin
from .models import HomeWork,Answer
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['Title_homework','student_number','File','last_post_time','score']
# Register your models here.
admin.site.register(HomeWork)
admin.site.register(Answer,AnswerAdmin)