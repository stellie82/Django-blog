from django.forms import ModelForm
from blogging.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'text', 'notes']
