from django.contrib import admin
from .models import ResumeTemplate, Resume

@admin.register(ResumeTemplate)
class ResumeTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_id', 'category', 'usage_count')
    list_filter = ('category',)
    search_fields = ('name', 'template_id')
    readonly_fields = ('usage_count',)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'template', 'ats_score', 'created_at')
    list_filter = ('template', 'created_at')
    search_fields = ('title', 'user__username')
