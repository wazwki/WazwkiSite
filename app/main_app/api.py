''' API for main app '''
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ContactSerializer
from .models import Contact


class ContactViewSet(ModelViewSet):
    ''' API for contact form '''
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['id']
    search_fields = ['vacancy', 'description_vacancy']
    orderindg_fields = ['id']
