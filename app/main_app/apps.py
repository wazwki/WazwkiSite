"""
Module containing the configuration for the main_app application.
"""

from django.apps import AppConfig

class MainAppConfig(AppConfig):
    """
    Configuration for the main_app application.

    This class represents the configuration for the main_app application in Django.
    It sets the default auto field and the name of the application.

    Attributes:
        default_auto_field (str): The default auto field for the application.
        name (str): The name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'
