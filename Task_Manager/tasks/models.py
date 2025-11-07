from django.db import models
from django.utils import timezone
from users.models import TaskUsers


class Task(models.Model):
    """
    Creating a model to store the tasks

    Attributes:
    Task Title(Charfield): field contain the task name
    Task Description(TextField): field contain the description
    User_id(foreign key): to know the owner of the task
    priority(Integer Field): to know the priorty task, use choices
    task_time(datetime field): to get the task time
    status(integer field): to know the task status created, in progress, cancelled
    is_deleted(BooleanField): to know the task is deleted 
    is_archieved(BooleanField): to know the task is archieved
    subtask(foreignkey): to the same model and it lists all the subtasks. if its none the it shows its a main task
    """
    class Meta:
        ordering = ['-created_at']

    class Priority(models.IntegerChoices):
        LOW = 1, 'Low'
        MEDIUM = 2, 'Medium'
        HIGH = 3, 'High'

    class Status(models.IntegerChoices):
        CREATED = 1, 'Created'
        IN_PROGRESS = 2, 'In Progress'
        COMPLETED = 3, 'Completed'
        CANCELLED = 4, 'Cancelled'

    task_title = models.CharField(max_length=50)
    task_description = models.TextField(blank=True)
    task_user = models.ForeignKey(TaskUsers, on_delete=models.CASCADE, related_name='tasks')
    priority = models.IntegerField(choices=Priority.choices, default=Priority.MEDIUM)
    task_time = models.DateTimeField(default=timezone.now)
    task_status = models.IntegerField(choices=Status, default=Status.CREATED)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, related_name="sub_tasks", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_title


class TaskActivity(models.Model):
    """
    creates an activity log

    Attributes:
    activity_title(CharField): to hold the task name
    task(ForeignKey): to get the task or subtask of related activity
    created_at(datetime field): to get the activity performed time
    """
    activity_title = models.CharField(max_length=50)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_activity')
    task_user = models.ForeignKey(TaskUsers, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_title
    

class Comments(models.Model):
    """
    creates comments of the tasks

    Attributes:
    Comment(TextField): stores the comment
    task(ForeignKey): to get the task or subtask of related activity
    created_at(datetime field): to get the activity performed time
    """
    class Meta:
        ordering = ['-created_at']

    comments = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(TaskUsers, on_delete=models.SET_NULL, null=True, blank=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
