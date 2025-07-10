from . import views
from django.urls import path


urlpatterns = [
    path("", views.TaskListView.as_view(), name="todo-home"),
    path("update/", views.reorder_task, name="update-task-order"),
    path("add/", views.TaskCreateView.as_view(), name="todo-add"),
    path("delete/<int:pk>/", views.TaskDeleteView.as_view(), name="todo-delete"),
    path("about/", views.about, name="todo-about"),
]