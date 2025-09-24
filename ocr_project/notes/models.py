from django.db import models
# notes/models.py
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)  # allow null temporarily
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='notes/')
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title