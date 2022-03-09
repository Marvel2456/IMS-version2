from django.apps import AppConfig


class ImsConfig(AppConfig):
    name = 'ims'
    
    def ready(self):
        import ims.signals
