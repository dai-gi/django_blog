from django.views.generic import View
from django.shortcuts import render
from .models import Post


class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by("-id")
        return render(request, 'blog/index.html', {
            'post_data': post_data,
        })