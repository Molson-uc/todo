from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm


def list_tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"tasks": tasks, "form": form}
    return render(request, "tasks/list.html", context)


def update_task(request, _id):
    task = Task.objects.get(id=_id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "tasks/update.html", {"form": form})


def delete_task(request, _id):
    task = Task.objects.get(id=_id)
    if request.method == "POST":
        task.delete()
        return redirect("/")
    return render(request, "tasks/delete.html", {"task": task})
