import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.apps import apps as django_apps

class Command(BaseCommand):
    help = "Deletes migration files for the specified app"

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='The name of the app to delete migration files from')

    def handle(self, *args, **options):
        app_name = options['app_name']

        # Check if the app is in INSTALLED_APPS
        if app_name not in settings.INSTALLED_APPS:
            raise CommandError(f'App "{app_name}" is not in INSTALLED_APPS')

        # Ensure it's not a built-in Django app
        built_in_apps = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            # Add other built-in apps if necessary
        ]

        if app_name in built_in_apps:
            raise CommandError(f'App "{app_name}" is a built-in Django app and cannot be modified')

        # Get the app config
        try:
            app_config = django_apps.get_app_config(app_name)
        except LookupError:
            raise CommandError(f'App "{app_name}" does not exist')

        # Find the migration folder
        migration_folder = os.path.join(app_config.path, 'migrations')
        if not os.path.exists(migration_folder):
            raise CommandError(f'Migration folder for app "{app_name}" does not exist')

        # Delete the migration files
        for filename in os.listdir(migration_folder):
            if filename != '__init__.py':  # Keep the __init__.py file
                file_path = os.path.join(migration_folder, filename)
                os.remove(file_path)
                self.stdout.write(self.style.SUCCESS(f'Successfully deleted {file_path}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted migration files for app "{app_name}"'))
