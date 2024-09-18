from django.db import models
from django.contrib.auth.models import User  # Using Django's built-in User model

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_year = models.CharField(max_length=4)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    image_url = models.TextField(blank=True, null=True)  # URL for the image
    pdf_link = models.TextField(blank=True, null=True)  # URL for the image
    video_url = models.URLField(blank=True, null=True)  # URL for the video

    def __str__(self):
        return self.title

# Tutorial Model
class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutorials')
    image_url = models.URLField(max_length=500, blank=True, null=True)  # URL for the image
    video_url = models.URLField(max_length=500, blank=True, null=True)  # URL for the video

    def __str__(self):
        return self.title
