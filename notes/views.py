from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    """
    Handles GET and POST requests.
    - GET: Returns a list of all notes.
    - POST: Creates a new note.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET, PUT, and DELETE requests for a single note.
    - GET: Retrieves a specific note.
    - PUT: Updates a note.
    - DELETE: Deletes a note.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer