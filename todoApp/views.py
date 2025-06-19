from datetime import timezone
from django.utils import timezone
from django.shortcuts import render
from .forms import ToDoForm


def home(request):
    return render(request, 'home.html')

def statusUpdate(request, pk):
    todo = CreateTodo.objects.get(pk=pk)
    todo.isComplete = not todo.isComplete
    todo.save()
    return redirect('todo_list')


from django.shortcuts import render, redirect, get_object_or_404
from .models import CreateTodo

# def todo_list(request):
#     todos = CreateTodo.objects.all
#     return render(request, 'home.html', {'todos': todos})

def todo_list(request):
    todos = CreateTodo.objects.filter(isDeleted=False)
    return render(request, 'home.html', {'todos': todos})


def create_todo(request):
    form = ToDoForm()
    
    if request.method == 'POST':
         form = ToDoForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('todo_list')  
           
    context = {
        'form': form
    }
    
    return render(request, 'addData.html', context)


def update_todo(request, pk):
    todo = get_object_or_404(CreateTodo, id=pk)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
        
    form = ToDoForm(instance=todo)     
    return render(request, 'edit.html', {'form': form, 'todo': todo})
 
 
 
 
 
def soft_delete(request, pk):
    todo = get_object_or_404(CreateTodo, pk=pk)
    todo.isDeleted = True
    todo.deleted_at = timezone.now()
    todo.save()
    return redirect('todo_list')

def trash_list(request):
    todos = CreateTodo.objects.filter(isDeleted=True)
    return render(request, 'trash.html', {'todos': todos})

def restore_todo(request, pk):
    todo = get_object_or_404(CreateTodo, pk=pk)
    todo.isDeleted = False
    todo.deleted_at = None
    todo.save()
    return redirect('todo_list')

def delete_permanently(request, pk):
    todo = get_object_or_404(CreateTodo, pk=pk)
    todo.delete()
    return redirect('trash_list')