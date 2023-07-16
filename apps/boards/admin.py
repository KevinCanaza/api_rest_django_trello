from django.contrib import admin

from apps.boards.models import *


# Register your models here.

admin.site.register(Board)
admin.site.register(TaskList)
admin.site.register(Task)