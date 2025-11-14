from django.shortcuts import render
from rest_framework import mixins, generics
from .serializers import (
    TaskSerializer, 
    TaskActivitySerializer, 
    CommentSerializer, 
    ReminderSerializers)
from .models import Task


class Tasks(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
