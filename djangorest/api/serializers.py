from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into JSON format"""

    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        """Meta class to map serializer's fields with model fields"""
        model = Bucketlist
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
        
