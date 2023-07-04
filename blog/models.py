from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #double under score to be more descriptive on what we want to see when the query is displayed
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# post = Post.objects.get(pk=1)  # Retrieve the post object
# url = reverse('post-detail', kwargs={'pk': post.pk})  # Get the URL for post-detail view with the post's primary key