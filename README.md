# Django Migration Cleaner

Django Migration Cleaner is a Django management command that allows you to easily delete migration files for specified apps or for all apps within your Django project. This can be useful for cleaning up your project during development.

## Features

- Delete migration files for specified apps.
- Delete migration files for all apps within the project.
- Ensures built-in Django apps are not modified.


## Installation

You can install Django Migration Cleaner via pip:

```bash
pip install django-migration-cleaner
```

Add django_migration_cleaner to your INSTALLED_APPS in your Django project's settings.py:

```python
INSTALLED_APPS = [
    ...
    'django_migration_cleaner',
    ...
]
```

Usage

Delete Migrations for Specific Apps
To delete migration files for specific apps, run the following command:

```python
python manage.py delete_migrations app_name1 app_name2
```

Replace app_name1, app_name2, etc. with the names of the apps for which you want to delete the migration files.

#### Delete Migrations for All Apps<br />
To delete migration files for all apps within your Django project, run the following command:

```python
python manage.py delete_migrations --all
```

Example
```python
python manage.py delete_migrations myapp anotherapp
```

This will delete all migration files for myapp and anotherapp, except for the __init__.py files in their migration directories.

#### Contributing

##### Contributions are welcome! Please feel free to submit a Pull Request.

- Steps to Contribute
- Fork the repository.
- Create your feature branch (git checkout -b feature/YourFeature).
- Commit your changes (git commit -am 'Add some feature').
- Push to the branch (git push origin feature/YourFeature).
- Create a new Pull Request.
- License

This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements

This project was inspired by the need to clean up migration files during Django project development.

#### Contact

For any questions or suggestions, feel free to open an issue or contact the project maintainer.