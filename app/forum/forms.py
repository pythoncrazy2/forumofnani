<<<<<<< HEAD
from django import forms

from .models import Comment, Topic

class CreateTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title', 'description'
        ]

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body', 'author', 'post'
=======
from django import forms

from .models import Comment, Topic

class CreateTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title', 'description'
        ]

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body', 'author', 'post'
>>>>>>> 0f2e3bf08cb23908bad5d4911f58b073ee1a305b
        ]