from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def index(request):

    if request.method == "POST":
        title = request.POST.get("title")

        if title:
            Task.objects.create(title=title)

        return redirect('/')

    tasks = Task.objects.all()

    return render(request, "index.html", {"tasks": tasks})


def update_task(request, id):

    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.save()

        return redirect('/')

    return render(request, "update.html", {"task": task})


def delete_task(request, id):

    task = get_object_or_404(Task, id=id)
    task.delete()

    return redirect('/')


def complete_task(request, id):

    task = get_object_or_404(Task, id=id)

    task.completed = not task.completed
    task.save()

    return redirect('/')

