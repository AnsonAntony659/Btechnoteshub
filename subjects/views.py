from django.shortcuts import render
from .models import Department,Semester
from year . models import Year
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


def semester_list(request, year_id):
    year = Year.objects.get(id=year_id)

    semesters = Semester.objects.filter(
        year=year
    )

    context = {
        "year": year,
        "semesters": semesters,
    }

    return render(
        request,
        "subjects/semester_list.html",
        context,
    )