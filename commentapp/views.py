from django.shortcuts import render

# Create your views here.
from django.template.defaulttags import comment
from django.urls import reverse
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.forms import CommentCreationForm


class CommentCreateView(CreateView):
    model = comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.article_id = self.request.POST.get('article_pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})

class CommentDeleteView(DeleteView):
    model = comment
    context_object_name = 'target_comment'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})