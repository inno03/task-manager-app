from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  Class Meta:
    