from django.db import models

class Year(models.Model):
    scheme = models.ForeignKey(
        'scheme.Scheme',
        on_delete=models.CASCADE
    )
    number = models.IntegerField()

    def __str__(self):
        return f"Year {self.number}"