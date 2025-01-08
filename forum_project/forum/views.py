from django.shortcuts import render, get_object_or_404
from .models import Category, Thread, Reply
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import ThreadForm, ReplyForm

def home(request):
    categories = Category.objects.all()
    return render(request, 'forum/home.html', {'categories': categories})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    replies = Reply.objects.filter(thread=thread).order_by('created_at')  
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'replies': replies})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'forum/signup.html', {'form': form})

@login_required
def create_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.author = request.user
            thread.save()
            return redirect('thread_detail', thread_id=thread.id)
    else:
        form = ThreadForm()
    return render(request, 'forum/create_thread.html', {'form': form})

@login_required
def add_reply(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.thread = thread
            reply.author = request.user
            reply.save()
            return redirect('thread_detail', thread_id=thread.id)
    else:
        form = ReplyForm()
    return render(request, 'forum/add_reply.html', {'form': form, 'thread': thread})

def category_threads(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    threads = Thread.objects.filter(category=category)
    return render(request, 'forum/category_threads.html', {
        'category': category,
        'threads': threads,
    })