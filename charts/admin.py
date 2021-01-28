from django.contrib import admin
from .models import TestResult


class TestResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'test_result', 'test_date']
    list_display_links = ['id', 'test_result']
    search_fields = ['test_result', 'test_date']
    list_per_page = 25

admin.site.register(TestResult, TestResultAdmin)
