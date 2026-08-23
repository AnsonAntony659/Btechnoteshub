from django.urls import path
from . import views

urlpatterns = [
    path("<int:department_id>/", views.scheme_list, name="scheme_list"),
]