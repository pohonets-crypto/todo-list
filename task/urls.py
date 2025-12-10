from django.urls import path

from task.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, toggle_task_status, TagListView, \
    TagCreateView, TagUpdateView, TagDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="homepage"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle/", toggle_task_status, name="task-toggle"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/tag-create/", TagCreateView.as_view(), name="tag-create"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete")

]

app_name = "task"