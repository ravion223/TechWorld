from django.apps import AppConfig


class AuthenticationSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication_system'

    def ready(self) -> None:
        import authentication_system.signals