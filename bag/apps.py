from django.apps import AppConfig


class BagConfig(AppConfig):
    name = 'bag'

    def ready(self):
        import checkout.signals