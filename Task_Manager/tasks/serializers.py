from rest_framework import serializers
from . models import Task, TaskActivity, Comments, Reminder


class TaskActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskActivity
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class ReminderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    task_activity = TaskActivitySerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'

