"""
models/classes are
defined here
"""

from django.shortcuts import reverse
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
        return str(self.title)

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
    approved = models.BooleanField(default=True)

    class Meta:
        """
        class to organise comments
        to the comment date (ascending order)
        """
        ordering = ['created_on']

    def __str__(self):
        """
        return this object in
        string form
        """
        return f"comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """
        return absolute url
        """
        return reverse('home')


class CommentValidator():
    """
    class to validate number of
    characters in each comment
    """
    def validate(self, text):
        """
        validates the text entered
        """

        if len(text) > 1000:
            return 'Your comment is too long.'
        else:
            return ''
