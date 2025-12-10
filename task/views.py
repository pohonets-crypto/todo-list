from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from task.forms import TaskForm
from task.models import Task, Tag


# Create your views here.
class TaskListView(generic.ListView):
    model = Task
    template_name = "task/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.order_by("is_done", "-created_at").prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:homepage")



class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:homepage")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:homepage")


class ToggleTaskStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("task:homepage")


class TagListView(generic.ListView):
    model = Tag
    template_name = "task/tag_list.html"

    def get_queryset(self):
        return Tag.objects.order_by("name")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")
