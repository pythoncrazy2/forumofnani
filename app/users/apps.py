<<<<<<< HEAD
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
=======
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
>>>>>>> 0f2e3bf08cb23908bad5d4911f58b073ee1a305b
