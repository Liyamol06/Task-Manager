from django.contrib import admin
from .models import Task, TaskActivity, Comments, Reminder

admin.site.register(Task)
admin.site.register(TaskActivity)
admin.site.register(Comments)
admin.site.register(Reminder)
