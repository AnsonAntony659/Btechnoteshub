from django.urls import path
from . import views

urlpatterns = [
    path("departments/<int:course_id>/", views.department_list, name="department_list"),
    path("semesters/<int:year_id>/", views.semester_list, name="semester_list"),
    path("subjects/<int:semester_id>/",views.subject_list,name="subject_list"),
]