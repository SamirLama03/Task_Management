from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

def home(request): 
    return render(request, 'tasks/home.html')

@login_required
def task_list(request):
    """View to display a list of tasks with sorting options."""
    status = request.GET.get('status')
    priority = request.GET.get('priority')

    tasks = Task.objects.filter(
        created_by=request.user
    ) | Task.objects.filter(
        assigned_to=request.user
    )

    if status:
        tasks = tasks.filter(status=status)
    if priority:
        tasks = tasks.filter(priority=priority)

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    """View to display the details of a specific task."""
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_create(request):
    """View to create a new task."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            # Redirect to the task list after the task is created
            return redirect('tasklist')  # Ensure 'tasklist' is the correct URL name

    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form})
@login_required
def task_update(request, task_id):
    """View to update an existing task."""
    task = get_object_or_404(Task, id=task_id)

    # Check if the task was created by the logged-in user
    if task.created_by != request.user:
        return redirect('tasklist')  # You can adjust the redirect if needed

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})

@login_required
def task_delete(request, task_id):
    """View to delete a task."""
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasklist')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
