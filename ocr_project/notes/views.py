from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note
import pytesseract
from PIL import Image

def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            # Perform OCR
            image = Image.open(note.image)
            note.text = pytesseract.image_to_string(image)
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/upload.html', {'form': form})

def note_list(request):
    notes = Note.objects.all()
    query = request.GET.get('q')
    if query:
        notes = notes.filter(text__icontains=query)
    return render(request, 'notes/list.html', {'notes': notes})
