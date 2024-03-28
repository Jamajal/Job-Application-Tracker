from rest_framework import serializers
from .models import JobApplication

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id', 'company', 'role', 'local', 'modality', 'link', 'observation', 'created_at', 'updated_at']
