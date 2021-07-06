from django.contrib import admin

# Register your models here.
from todolist.models import TaskItem, Project

class TaskItemAdmin(admin.ModelAdmin):
    list_display = ["title", "due_date", "creation_date", "description", "project"]
    list_filter = ["title"]
    search_fields = ["title"]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "owner"]
    list_filter = ["name", "owner"]
    search_fields = ["name"]




admin.site.register(TaskItem, TaskItemAdmin)
admin.site.register(Project, ProjectAdmin)