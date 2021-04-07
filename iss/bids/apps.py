from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BidsConfig(AppConfig):
    name = "iss.bids"
    verbose_name = _("Bids")

    def ready(self):
        try:
            import iss.users.signals  # noqa F401
        except ImportError:
            pass
