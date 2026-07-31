from django.db import models
from universities.models import University


class Course(models.Model):
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name