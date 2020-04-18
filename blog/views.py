from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get_queryset(self):
        # return Post.objects.all()
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class CreatePostView(LoginRequiredMixin, CreateView):
	login_url = '/login/'
	template_name = "blog/post_form.html"
	redirect_field_name = 'blog/post_detail.html'
	form_class = PostForm
	model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
	login_url = '/login/'
	template_name = "blog/post_form.html"
	redirect_field_name = 'blog/post_detail.html'
	form_class = PostForm
	model = Post

class DraftListView(LoginRequiredMixin, ListView):
	login_url = '/login/'
	template_name = 'blog/post_draft_list.html'
	model = Post

	def get_queryset(self):
		return Post.objects.filter(published_date__isnull=True).order_by('created_date')

@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)

class PostDeleteView(LoginRequiredMixin, DeleteView):
	model = Post
	template_name = "blog/post_confirm_delete.html"
	success_url = reverse_lazy('post_list')

