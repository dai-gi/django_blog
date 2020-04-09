from django.utils import timezone
from blog.models import Post
from django.views.generic import (ListView)


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')