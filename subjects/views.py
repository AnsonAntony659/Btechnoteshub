from django.shortcuts import render, get_object_or_404
from .models import Department,Semester,Subject
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


def subject_list(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)

    subjects = Subject.objects.filter(semester=semester)

    return render(
        request,
        "subjects/subject_list.html",
        {
            "semester": semester,
            "subjects": subjects,
        },
    )