from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm
from .forms import Comment
from .models import CommentValidator


class UpdateCommentView(UpdateView):
    """
    A view to allow us to use django
    generic UpdateView view to update
    the Comment model
    """
    model = Comment
    template_name = 'update_comment.html'
    fields = ['body']


class DeleteCommentView(DeleteView):
    """
    A view to allow us to use django
    generic UpdateView view to delete
    the Comment model
    """
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('home')


class PostList(generic.ListView):
    """
    A class to provide a View
    to a list of Posts
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-post_create_date')
    template_name = 'index.html'
    paginate_by = 4


class PostDetail(View):
    """
    A class to provide a View
    to details about a Post
    """

    def get(self, request, slug, *args, **kwargs):
        """
        A function to respond to a Get method
        on this class, returning all details
        of a Post
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        A function to respond to a
        post request to this class,
        saving any comments made to
        the Post
        """

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        commented = True
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username

            comment = comment_form.save(commit=False)
            comment.approved = True
            validator = CommentValidator()
            validation_message = validator.validate(comment.body)

            if len(validation_message) == 0:
                comment.post = post
                comment.save()
            else:
                commented = False

            comment_form = CommentForm()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": commented,
                "comment_form": comment_form,
                "comment_id": comment.id,
                "liked": liked,
                "validation_message": validation_message
            },
        )


class About(View):
    """
    A view to allow us render the About page
    """
    def get(self, request, *args, **kwargs):
        """
        A function to respond to a Get method
        on this class, returning the about page
        """
        return render(
            request,
            "about.html",
        )


class PostLike(View):
    """
    A class returning a View
    to likes on a Post
    """

    def post(self, request, slug):
        """
        A function to increment or decrement
        the number of likes on a Post. If
        incrementing it associates that like
        with a User.
        """
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
