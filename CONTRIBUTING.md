# Contributing

## Run template tests

Requires [tox](https://tox.wiki).

To create a test project and run the Python tests:
```console
$ tox -e create
```

To rerun the Python tests without recreating the test project:
```console
$ tox
```

To run the TypeScript tests (requires [Node.js](https://nodejs.org)):
```console
$ cd test_project
$ npm install
$ npm test
$ npm run lint
```

The above tests are run automatically by GitHub Actions following a `git push`
(see [test.yml](.github/workflows/test.yml)).

## Adding new files with template tags

If you introduce a non-Python file which needs to be templated (e.g. they use the
`{{ project_name }}` template tag) ensure the corresponding file extension is included
in the following places:

- [README.md - Usage](README.md#usage)
- [scripts/manage_test_project.py](scripts/manage_test_project.py)

## Checking for default template changes between Django releases

The default templates used by `django-admin startproject` and `django-admin startapp`
can be different depending on the version of `Django` used. It can be useful to know
what changes are being made upstream. To generate diffs between default templates from
different Django versions:

1. Download the template for a specific Django version e.g. `3.0.7`:
   ```console
   $ git init
   $ git remote add upstream git@github.com:django/django.git
   $ git fetch --depth 1 upstream tag 3.0.7
   $ git checkout 3.0.7 -- django/conf/project_template
   ```
2. Generate a diff with a different Django version e.g. between `3.0.7` and `3.0.8`:
   ```console
   $ git fetch --depth 1 upstream tag 3.0.8
   $ git diff 3.0.7 3.0.8 django/conf/project_template
   ```

## Other checks

- [`.gitignore`](project_template/.gitignore): copied from
  https://github.com/github/gitignore/blob/main/Python.gitignore.

## Release new template versions

1. Select a new version identifier. Versions must be a
   [Python version identifier](https://peps.python.org/pep-0440/#version-scheme).
2. Update the release version in the [README's Usage section](README.md#usage).
3. A release is performed automatically using GitHub Actions (see
   [release.yml](.github/workflows/release.yml)). To trigger a release create a tag
   which begins with the letter `v` followed by the version identifier, for example:
   ```console
   $ git tag v0.1 -m v0.1
   $ git push origin v0.1
   ```
