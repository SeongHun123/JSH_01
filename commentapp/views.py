from django.shortcuts import render

# Create your views here.
from django.template.defaulttags import comment
from django.urls import reverse
from django.views.generic import CreateView

from commentapp.forms import CommentCreationForm


class CommentCreateView(CreateView):
    model = comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})