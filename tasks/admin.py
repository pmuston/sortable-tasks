from django.contrib import admin

# Register your models here.
from .models import TaskList, Task

admin.site.register(TaskList)
admin.site.register(Task)
