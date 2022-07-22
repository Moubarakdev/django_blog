from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm


# Create your views here.

class BlogHome(ListView):
    model = BlogPost
    context_object_name = "posts"

    # recuperer les données de la base de données
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = 'post'


@method_decorator(login_required, name="dispatch")
class BlogPostCreate(CreateView):
    model = BlogPost
    context_object_name = 'form'
    template_name = "posts/blogpost_create.html"
    #form_class = BlogPostForm
    fields = ['title', 'content', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["submit_text"] = "Créer"
        return context

@method_decorator(login_required, name="dispatch")
class BlogPostUpdate(UpdateView):
    model = BlogPost
    context_object_name = 'form'
    template_name = "posts/blogpost_create.html"
    #form_class = BlogPostForm
    fields = ['title', 'content', 'published']

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["submit_text"] = "Modifier"
        return context

@method_decorator(login_required, name="dispatch")
class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = 'post'
    success_url = reverse_lazy("posts:home")