from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    age_group = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    file = models.FileField(storage=RawMediaCloudinaryStorage(), blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# books/models.py

class ReadingExercise(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title
