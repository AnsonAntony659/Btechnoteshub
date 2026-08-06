from django.urls import path
from . import views

urlpatterns = [
    path("<int:university_id>/", views.course_list, name="course_list"),
]