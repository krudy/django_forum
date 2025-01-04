from django.shortcuts import render, get_object_or_404
from .models import Category, Thread, Reply

def home(request):
    categories = Category.objects.all()
    return render(request, 'forum/home.html', {'categories': categories})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    return render(request, 'forum/thread_detail.html', {'thread': thread})
