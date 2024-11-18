from setuptools import setup, find_packages

setup(
    name="django-migration-cleaner",
    version="0.0.1",  
    author="Devjoseph",
    author_email="joseph4jubilant@gmail.com",
    description="A Django management command to delete migrations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/django-migration-cleaner",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "django>=3.2",
    ],
    entry_points={
        "console_scripts": [
            "django-migration-cleaner=django_migration_cleaner.main_script:main",
        ],
    },
    include_package_data=True,
)
