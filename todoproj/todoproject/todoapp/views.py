from django.shortcuts import render
from .models import TodoListItem 
from django.http import HttpResponseRedirect


# Create your views here.
def todoappView(request):
    return render(request,'todolist.html')

def addTodoView(request):
    X = request.POST['content']
    new_item = TodoListItem(content = X)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')
