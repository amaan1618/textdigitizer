from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='notes/')
    text = models.TextField(blank=True)  # OCR result
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title