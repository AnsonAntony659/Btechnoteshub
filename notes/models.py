from django.db import models
from django.contrib.auth.models import User
from subjects.models import Subject


class Note(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title