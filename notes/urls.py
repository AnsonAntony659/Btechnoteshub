from django.urls import path
from . import views

urlpatterns = [
    path(
        "<int:subject_id>/",
        views.note_list,
        name="note_list"
    ),

    path(
        "download/<int:note_id>/",
        views.download_note,
        name="download_note"
    ),
]