from django.apps import AppConfig


class {{ camel_case_project_name }}AppConfig(AppConfig):
    name = "{{ project_name }}_app"
    default_auto_field = "django.db.models.BigAutoField"
