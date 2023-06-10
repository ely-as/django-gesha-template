# django-gesha-template

[![Test](https://github.com/ely-as/django-gesha-template/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/ely-as/django-gesha-template/actions/workflows/test.yml)

Generate [Django](https://www.djangoproject.com/) projects which use
[django-gesha](https://github.com/ely-as/django-gesha) (a package which provides
JavaScript utilities).

## Usage

[Install Django](https://docs.djangoproject.com/en/stable/intro/install/) and use the
[`django-admin startproject`](https://docs.djangoproject.com/en/stable/ref/django-admin/#startproject)
command.

For example, to create a project named `myproject`:
```sh
django-admin startproject myproject \
--extension js,json,md,py,toml \
--template https://github.com/ely-as/django-gesha-template/releases/download/v0.1a2/django-gesha-template.zip
```

And then follow the installation instructions in the README of your newly created
project.

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md).
