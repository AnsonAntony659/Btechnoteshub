from django.shortcuts import render
from .models import Course
from universities.models import University


def course_list(request, university_id):
    university = University.objects.get(id=university_id)

    courses = Course.objects.filter(
        university=university
    )

    context = {
        "university": university,
        "courses": courses,
    }

    return render(
        request,
        "courses/course_list.html",
        context,
    )