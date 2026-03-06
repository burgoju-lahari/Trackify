from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(
                title=title,
                user = request.user
                )

        return redirect('task_list')

    tasks = Task.objects.filter(user = request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id, user= request.user) #user= request.user, so only users can touch their tasks

    if request.method == 'POST':
        task.completed = not task.completed
        task.save()

    return redirect('task_list')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user= request.user)
    task.delete()
    return redirect('task_list')

@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id, user= request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task.title = title
            task.save()
        return redirect('task_list')

    return render(request, 'tasks/edit_task.html', {'task': task})