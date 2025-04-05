from django.contrib import admin
from .models import Note  # Import the Note model from models.py

admin.site.register(Note)  # Register the Note model with the admin site