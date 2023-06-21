# django-gesha-template

[![Test](https://github.com/ely-as/django-gesha-template/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/ely-as/django-gesha-template/actions/workflows/test.yml)

Generate [Django](https://www.djangoproject.com/) projects which use
[django-gesha](https://django-gesha.readthedocs.io) (a package which provides
JavaScript utilities).

Features:
- Start your project with clean TypeScript and Sass integration.
- Generates both a project and an installed app.
- Starts you off with a functioning website (all tests passing) so you can start with a
  working state.

Comes configured with:
- Python tools:
  - [pytest](https://docs.pytest.org) for unit tests with
    [coverage](https://coverage.readthedocs.io).
  - [mypy](https://mypy.readthedocs.io) for static type checking.
  - [ruff](https://beta.ruff.rs/docs/) for linting and code formatting.
  - [black](https://black.readthedocs.io) for code formatting.
- TypeScript tools:
  - [Mocha](https://mochajs.org/) for unit tests.
  - [ESLint](https://eslint.org/) for linting.
  - [django-gesha](https://django-gesha.readthedocs.io) for easy integration with
    Django.
- [Gulp](https://gulpjs.com/) pipelines for:
  - Compiling [TypeScript](https://www.typescriptlang.org/) with
    [Browserify](https://browserify.org/) to a minified JavaScript bundle.
  - Compiling [Sass](https://sass-lang.com/documentation/) to minified CSS.

## Usage

1. [Install Django](https://docs.djangoproject.com/en/stable/intro/install/).
2. Call
   [`django-admin startproject`](https://docs.djangoproject.com/en/stable/ref/django-admin/#startproject)
   with the `--extension` and `--template` options. For example, to create a project
   named `myproject` using the
   [latest release](https://github.com/ely-as/django-gesha-template/releases):

   ```sh
   django-admin startproject myproject \
   --extension js,json,md,py,toml \
   --template https://github.com/ely-as/django-gesha-template/releases/download/v0.1a4/django-gesha-template.zip
   ```

3. In the newly created project:
   - Follow the installation instructions in the generated `README.md`.
   - See the generated `CONTRIBUTING.md` for additional setup required for development.

**Note:** If `startproject` fails to download the URL you can download the ZIP file
manually and use `--template` with a local path.

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md).

## License

[MIT](LICENSE).
