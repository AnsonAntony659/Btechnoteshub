from django.shortcuts import render
from .models import Scheme
from subjects.models import Department


def scheme_list(request, department_id):
    department = Department.objects.get(id=department_id)

    schemes = Scheme.objects.filter(
        department=department
    )

    context = {
        "department": department,
        "schemes": schemes,
    }

    return render(
        request,
        "scheme/scheme_list.html",
        context,
    )