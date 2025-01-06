from django import forms
from .models import Thread, Reply

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content', 'category']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
