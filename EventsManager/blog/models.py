from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True) # SlugField is a field for storing URLs
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # ForeignKey is a field for defining a one-to-many relationship
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False) # DateTimeField is a field for storing date and time
    updated_at = models.DateTimeField(auto_now=True) # auto_now_add=True means that the date and time will be saved automatically when creating an object
    status = models.CharField(max_length=10, choices=options, default='draft') # CharField is a field for storing text data
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
