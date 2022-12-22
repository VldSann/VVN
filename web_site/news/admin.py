from django.contrib import admin
from .models import Articles


class ArticlesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Название', {'fields': ['title']}),
        ('Год издания', {'fields': ['anons']}),
        ('ФИО Автора', {'fields': ['full_text']}),
        ('Дата публикации', {'fields': ['date']}),
    ]
    list_display = ('title', 'date', 'was_published_recently')
    list_filter = ['date']
    search_fields = ['title']


admin.site.register(Articles, ArticlesAdmin)
