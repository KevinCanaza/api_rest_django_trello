from django.contrib import admin

from apps.boards.models import *


# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id','title')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(Board,BoardAdmin)
admin.site.register(TaskList,TaskListAdmin)
admin.site.register(Task,TaskAdmin)