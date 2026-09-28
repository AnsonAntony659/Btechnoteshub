from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from subjects.models import Subject
from .models import Note


def note_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)

    notes = Note.objects.filter(subject=subject)

    return render(
        request,
        "notes/note_list.html",
        {
            "subject": subject,
            "notes": notes,
        },
    )

def download_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    return FileResponse(
        note.file.open("rb"),
        as_attachment=True,
        filename=note.file.name.split("/")[-1],
    )