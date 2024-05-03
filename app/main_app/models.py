''' Register models for mainapp '''

from django.db import models


class Contact(models.Model):
    ''' Models for contact form '''
    mail = models.EmailField(max_length=254)
    telegram = models.SlugField(max_length=254)
    vacancy = models.URLField()
    description_vacancy = models.TextField()
