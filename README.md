# django-gesha-template

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
--extension md,py,toml \
--template https://github.com/ely-as/django-gesha-template/releases/download/v0.1alpha0/django-gesha-template.zip
```

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md).
