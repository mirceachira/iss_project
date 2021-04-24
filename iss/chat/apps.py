from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ChatConfig(AppConfig):
    name = "iss.chat"
    verbose_name = _("Chat")

    def ready(self):
        try:
            import iss.users.signals  # noqa F401
        except ImportError:
            pass
