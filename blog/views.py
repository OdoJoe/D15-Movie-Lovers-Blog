from django.shortcuts import render
from django.views import generic
from .models import Post
from .models import Comment
from .models import Poll
from .models import PollOption


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-post_create_date')
    template_name = 'index.html'
    paginate_by = 4
