from django.db import models


class Department(models.Model):
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Semester(models.Model):
    year = models.ForeignKey(
        'year.Year',
        on_delete=models.CASCADE
    )
    number = models.IntegerField()

    def __str__(self):
        return f"Semester {self.number}"


class Subject(models.Model):
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE
    )
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name