from django.contrib import admin
from .models import Question, Choice

# class ChoiceAdmin(admin.ModelAdmin):
#     fields = ('choice_text', 'votes', 'question')
class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Choice',{
            'fields' : ('choice_text', 'votes'), 'classes' :['collapse']
        }),
        ('Question', {
            'fields' : ['question'], 'classes' :['collapse'] #파이썬 튜플은 하나짜리는 ,를 붙이거나 []로 넣어준다.
        }),
    )
    list_display = ('choice_text', 'question')
    list_filter = ('question',)
    search_fields = ('choice_text',)


admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)