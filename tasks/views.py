from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse

from tasks.models import TaskList, Task

class TaskListForm(ModelForm):
    class Meta:
        model = TaskList
        fields = ['name'] # add others

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority'] # add others

def tasklist_list(request, template_name='tasks/tasklist_list.html'):
    tasklists = TaskList.objects.all()
    data = {}
    data['object_list'] = tasklists
    return render(request, template_name, data)

def tasklist_create(request, template_name='tasks/tasklist_form.html'):
    form = TaskListForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tasklist_list')
    return render(request, template_name, {'form':form})

def tasklist_update(request, pk, template_name='tasks/tasklist_form.html'):
    tasklist = get_object_or_404(TaskList, pk=pk)
    form = TaskListForm(request.POST or None, instance=tasklist)
    if form.is_valid():
        form.save()
        return redirect('tasklist_list')
    return render(request, template_name, {'form':form})

def tasklist_delete(request, pk, template_name='tasks/tasklist_confirm_delete.html'):
    tasklist = get_object_or_404(TaskList, pk=pk)
    if request.method=='POST':
        tasklist.delete()
        return redirect('tasklist_list')
    return render(request, template_name, {'object':tasklist})

def tasklist(request, pk, template_name='tasks/tasklist.html'):
    task_list = get_object_or_404(TaskList, pk=pk)
    data = {}
    data['object'] = task_list
    data['tasks'] = Task.objects.filter(tasklist=task_list)
    return render(request, template_name, data)

def task_create(request, pk, template_name='tasks/task_form.html'):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        new_task = form.save(commit=False)
        tasklist = get_object_or_404(TaskList, pk=pk)
        new_task.tasklist = tasklist
        new_task.save()
        return redirect('tasklist', pk)
    return render(request, template_name, {'form':form})

def task_update(request, pk, template_name='tasks/task_form.html'):
    task = get_object_or_404(Task, pk=pk)
    form = TaskListForm(request.POST or None, instance=tasklist)
    if form.is_valid():
        form.save()
        return redirect('tasklist', task.tasklist_id)
    return render(request, template_name, {'form':form})

def task_delete(request, pk, template_name='tasks/task_confirm_delete.html'):
    task = get_object_or_404(Task, pk=pk)
    tasklist_id = task.tasklist_id
    if request.method=='POST':
        tasklist.delete()
        return redirect('tasklist', tasklist_id)
    return render(request, template_name, {'object':task})

def task_sort(request, pk, template_name=None):
    task_list = get_object_or_404(TaskList, pk=pk)
    tasks = Task.objects.filter(tasklist=task_list)
    if request.method=='POST':
        new_order = request.POST.getlist("task[]")
        new_order = [int(x) for x in new_order]
        print("New Order",new_order)
        print("Existing Order", task_list.get_task_order())
        task_list.set_task_order(new_order)
    return HttpResponse(status=200)
