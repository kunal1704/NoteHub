from django.db import models

class Note(models.Model): # model.Nodel is essentially a base class for all models in Django. It provides the functionality to create and manage database tables.
    
    title = models.CharField(max_length=255)  # A short title for the note
    content = models.TextField()  # The main content of the note
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created, auto_now_add ensures it's set only once
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when updated,auto_now ensures it's updated every time the object is saved

    def __str__(self):
        return self.title  # This defines how the note appears in Django Admin
