from django.urls import path
from .views import notes_list, note_detail

urlpatterns = [
    path('notes/', notes_list, name='notes_list'),  # List all notes or create a new note
    path('notes/<int:pk>/', note_detail, name='note_detail'),  # Fetch, update, or delete a specific note
]
