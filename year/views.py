from django.shortcuts import render, get_object_or_404
from .models import Year
from subjects.models import Semester
from scheme.models import Scheme


def year_list(request, scheme_id):
    scheme = get_object_or_404(Scheme, id=scheme_id)

    years = Year.objects.filter(scheme=scheme)

    context = {
        "scheme": scheme,
        "years": years,
    }

    return render(
        request,
        "year/year_list.html",
        context,
    )





def year_detail(request, year_id):
    year = get_object_or_404(Year, id=year_id)

    semesters = Semester.objects.filter(year=year)

    return render(
        request,
        "year/year_detail.html",
        {
            "year": year,
            "semesters": semesters,
        },
    )