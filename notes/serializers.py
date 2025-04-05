from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:  # we create this meta class to specify the model and fields we want to serialize i.e to configure the serializer
        model = Note
        fields = "__all__"
        
