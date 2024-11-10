from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published_date__isnull=False)

    def by_author(self, author):
        return self.get_queryset().filter(author=author)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Link to user as author
    published_date = models.DateTimeField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='posts')
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
