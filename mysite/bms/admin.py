from django.contrib import admin
from django.apps import apps

# Register your models here.
apps_config = apps.get_app_config('bms')
models = apps_config.get_models()

for model in models:
    admin.site.register(model)
