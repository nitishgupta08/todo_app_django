"""
Script to generate fixtures for all models in db
"""
import os

import sys

from django import setup
from django.apps import apps
from django.conf import settings
from django.core.management import call_command

DJANGO_PROJECT_PATH = os.path.dirname(os.getcwd())

sys.path.append(DJANGO_PROJECT_PATH)
os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings"

setup()


def generate_fixtures():
    fixture_path = settings.FIXTURE_DIRS[0]

    if not os.path.exists(fixture_path):
        os.makedirs(fixture_path)

    app_configs = apps.get_app_configs()

    for app_config in app_configs:
        app_name = app_config.name

        if 'django' in app_name:
            continue

        for model in app_config.get_models():
            model_name = model.__name__
            fixture_file = os.path.join(fixture_path, f'{model_name}_fixture.json')

            with open(fixture_file, 'w') as f:
                call_command('dumpdata', f'{app_name}.{model_name}', indent=4, stdout=f)

            print(f'Fixture generated for {app_name}.{model_name} at {fixture_file}')


if __name__ == '__main__':
    generate_fixtures()
