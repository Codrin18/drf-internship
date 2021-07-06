from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todolist import views
from .views import TaskItemViewSet, ProjectViewSet

app_name = "todo"
router = DefaultRouter()
router.register(r"taskitem", TaskItemViewSet)
router.register(r"project", ProjectViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('', views.list_tasks, name="list_tasks")
]