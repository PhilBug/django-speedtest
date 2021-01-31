from django.contrib import admin
from .models import TestResult


class TestResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'result', 'date', 'username']
    list_display_links = ['id', 'result']
    search_fields = ['result', 'date', 'username']
    list_per_page = 25

admin.site.register(TestResult, TestResultAdmin)
