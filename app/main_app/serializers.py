''' Serializers for mainapp '''
from rest_framework.serializers import ModelSerializer

from .models import Contact


class ContactSerializer(ModelSerializer):
    ''' Serializer for contact form '''
    class Meta:
        model = Contact
        fields = '__all__'
