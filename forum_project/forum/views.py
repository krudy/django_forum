from django.shortcuts import render, get_object_or_404
from .models import Category, Thread, Reply
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def home(request):
    categories = Category.objects.all()
    return render(request, 'forum/home.html', {'categories': categories})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    return render(request, 'forum/thread_detail.html', {'thread': thread})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'forum/signup.html', {'form': form})