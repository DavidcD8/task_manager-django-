from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import TaskSearchForm


# Create your views here.

# This view will allow users to register
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after registration
            return redirect('task_list')  # Change to your task list view name
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



# this view will list all the task avialable in the database
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    form = TaskSearchForm(request.GET or None)
    if form.is_valid():
        q = form.cleaned_data.get('q')
        completed = form.cleaned_data.get('completed')

        if q:
            tasks = tasks.filter(
                Q(name__icontains=q) | Q(description__icontains=q)
            )

        if completed in ['0', '1']:
            tasks = tasks.filter(completed=bool(int(completed)))

    # Pagination: 6 tasks per page
    paginator = Paginator(tasks, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'page_obj': page_obj,
    }
    return render(request, 'task_list.html', context)




# This view will add the data from the user form to the database as task
@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})



# This view loads the tasks from database allows editing and saves it
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.name = request.POST['name']
        task.description = request.POST['description']
        task.save()
        return redirect('task_list')
    return render(request, 'edit_task.html', {'task': task})



# This view will delete a task from the database
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_list')


# This view will mark the tasks as completed
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')