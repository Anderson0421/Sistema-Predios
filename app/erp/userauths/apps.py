from django.apps import AppConfig

class UserauthsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'erp.userauths'

    def ready(self):
        import erp.userauths.signals
