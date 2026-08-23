from django.shortcuts import render, get_object_or_404
from .models import Year
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