# notes/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note
import pytesseract
from PIL import Image

@login_required
def upload_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # Assign logged-in user
            image = Image.open(note.image)
            note.text = pytesseract.image_to_string(image)
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/upload.html', {'form': form})

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)  # Only current user’s notes
    query = request.GET.get('q')
    if query:
        notes = notes.filter(text__icontains=query)
    return render(request, 'notes/list.html', {'notes': notes})

from .forms import SignUpForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            return redirect('note_list')
    else:
        form = SignUpForm()
    return render(request, 'notes/signup.html', {'form': form})
