import os

from django.apps import apps as django_apps
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Deletes migration files for the specified apps or all apps if --all is specified"

    def add_arguments(self, parser):
        parser.add_argument(
            "app_names", nargs="*", type=str, help="The names of the apps to delete migration files from"
        )
        parser.add_argument("--all", action="store_true", help="Delete migration files for all apps")

    def handle(self, *args, **options):
        app_names = options["app_names"]
        delete_all = options["all"]

        if delete_all:
            self.delete_all_migrations()
        elif app_names:
            for app_name in app_names:
                self.delete_app_migrations(app_name)
        else:
            raise CommandError("You must provide at least one app name or use the --all flag.")

    def delete_app_migrations(self, app_name):
        if app_name not in settings.INSTALLED_APPS:
            raise CommandError(f'App "{app_name}" is not in INSTALLED_APPS')

        built_in_apps = [
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
        ]

        if app_name in built_in_apps:
            raise CommandError(f'App "{app_name}" is a built-in Django app and cannot be modified')

        try:
            app_config = django_apps.get_app_config(app_name)
        except LookupError:
            raise CommandError(f'App "{app_name}" does not exist')

        migration_folder = os.path.join(app_config.path, "migrations")
        if not os.path.exists(migration_folder):
            raise CommandError(f'Migration folder for app "{app_name}" does not exist')

        self.delete_migration_files(migration_folder)

        self.stdout.write(self.style.SUCCESS(f'Successfully deleted migration files for app "{app_name}"'))

    def delete_all_migrations(self):
        for app_config in django_apps.get_app_configs():
            if app_config.name not in settings.INSTALLED_APPS:
                continue

            migration_folder = os.path.join(app_config.path, "migrations")
            if not os.path.exists(migration_folder):
                continue

            self.delete_migration_files(migration_folder)

        self.stdout.write(self.style.SUCCESS("Successfully deleted migration files for all apps"))

    def delete_migration_files(self, migration_folder):
        for filename in os.listdir(migration_folder):
            if filename != "__init__.py":
                file_path = os.path.join(migration_folder, filename)
                os.remove(file_path)
                self.stdout.write(self.style.SUCCESS(f"Successfully deleted {file_path}"))
