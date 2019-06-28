from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from .models import Todo
from django import forms
from django.shortcuts import redirect
from .forms import AddNew
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
# @login_required
def todo_list(request):
	todos = Todo.objects.all().order_by('-priority', '-created_date')
	if request.method == "POST":
	    form = AddNew(request.POST)
	    if form.is_valid():
	        post = form.save(commit=False)
	        post.author = request.user
	        post.created_date = timezone.now()
	        post.save()
	        return redirect('todo_list')
	else:
	    form = AddNew()
	return render(request, 'routine/todo_list.html', {'form': form,'todos':todos})

def add_new_todo(request):
    if request.method == "POST":
        form = AddNew(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('todo_list')
    else:
        form = AddNew()
    return render(request, 'routine/todo_list.html', {'form': form})

def todo_complete(request, pk):
	todo = get_object_or_404(Todo,pk=pk).delete()
	return redirect('todo_list')
