from django.shortcuts import render
from .models import TodoListItem 


# Create your views here.
def todoappView(request):
    all_todo_items = TodoListItem.objects.all()

    return render(request, 'todolist.html',
    {'all_items' :all_todo_items})
