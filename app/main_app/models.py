''' Register models for mainapp '''

from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    ''' Models for contact form '''
    mail = models.EmailField(max_length=254)
    telegram = models.SlugField(max_length=254)
    vacancy = models.URLField()
    description_vacancy = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'id: {self.id}, {self.mail}'
