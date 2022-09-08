from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "DRAFT"), (1, "Published"))


class Post(models.Model):
    """
    Blog post class
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    post_create_date = models.DateTimeField(auto_now_add=True)
    post_update_date = models.DateTimeField(auto_now=True)
    post_content = models.TextField()
    post_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        class to organise posts
        to the post date (descending order)
        """
        ordering = ['-post_create_date']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """
        Returns post like count
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Blog posts comment class
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"comment {self.body} by {self.name}"


class Poll(models.Model):
    """
    Poll for users to select next months Director focus
    """
    date_active = models.DateTimeField()
    date_expire = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.body


class PollOption(models.Model):
    """
    Poll option to include image for user selection
    """
    poll_option_image = CloudinaryField('image', default='placeholder')
    poll_option_text = models.TextField()
    display_order = models.IntegerField()

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.poll_option_text
