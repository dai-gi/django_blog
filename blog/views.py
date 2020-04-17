from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (ListView, DetailView, CreateView, UpdateView)


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get_queryset(self):
        # return Post.objects.all()
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class CreatePostView(CreateView):
	template_name = "blog/post_form.html"
	redirect_field_name = 'blog/post_detail.html'
	form_class = PostForm
	model = Post

class PostUpdateView(UpdateView):
	template_name = "blog/post_form.html"
	redirect_field_name = 'blog/post_detail.html'
	form_class = PostForm
	model = Post

class DraftListView(ListView):
	login_url = '/login/'
	template_name = 'blog/post_draft_list.html'
	model = Post

	def get_queryset(self):
		return Post.objects.filter(published_date__isnull=True).order_by('created_date')

def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)
