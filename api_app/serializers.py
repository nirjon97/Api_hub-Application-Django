from rest_framework import serializers
from .models import Personal_info

class Personal_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_info
        fields = ['name', 'email', 'phone', 'fb_id']