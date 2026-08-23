from django.shortcuts import render
from .models import Department
from courses.models import Course


def department_list(request, course_id):
    course = Course.objects.get(id=course_id)

    departments = Department.objects.filter(
        course=course
    )

    context = {
        "course": course,
        "departments": departments,
    }

    return render(
        request,
        "subjects/department_list.html",
        context,
    )   