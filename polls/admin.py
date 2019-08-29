from django.contrib import admin

# Register your models here.
from .models import Choice, Question

# admin.site.register(Question)
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] # 增加pub_date排序功能
    search_fields = ['question_text'] # 增加搜尋功能


admin.site.register(Question, QuestionAdmin)
