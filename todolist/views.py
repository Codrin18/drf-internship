import json
from datetime import datetime

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet

from todolist.models import TaskItem, Project
from todolist.serializers import TaskItemSerializer, ProjectSerializer


@csrf_exempt
def list_tasks(request):
    if request.method == "GET":
        tasks = TaskItem.objects.all()
        task_list = [{"title": t.title, "due_date": t.due_date} for t in tasks]
        return JsonResponse(task_list, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        task_title = data.get("title")
        task_due_date = datetime.strptime(data.get("due_date"), "%Y-%m-%dT%H:%M:%S")
        task = TaskItem.objects.create(title=task_title, due_date=task_due_date)
        return JsonResponse({"title": task.title, "due_date": datetime.strftime(task.due_date, "%Y-%m-%dT%H:%M:%S")})

    return HttpResponse(status=405)

class TaskItemViewSet(ModelViewSet):
    serializer_class = TaskItemSerializer
    queryset = TaskItem.objects.all()

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()