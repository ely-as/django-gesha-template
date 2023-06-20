# Contributing

## Python development

### Setup

Install the additional packages used for Python development to your virtual environment:

```console
$ pip install -r requirements-test.txt
```

### Write and run unit tests

Python unit tests are located in the [tests](tests) directory.

To run unit tests using [pytest](https://docs.pytest.org) and report
[coverage](https://coverage.readthedocs.io) to terminal:

```console
$ pytest --cov-report=term
```

### Apply formatting

To apply [black](https://black.readthedocs.io) and
[isort](https://pycqa.github.io/isort/) formatting rules:

```console
$ black .
$ ruff check --select I --fix .
```

### Perform type checking

To perform static type checking using [mypy](https://mypy.readthedocs.io):

```console
$ mypy
```

### Linting

To lint Python code using [ruff](https://beta.ruff.rs/docs/):

```console
$ ruff check .
```

## TypeScript and Sass development

Source files for both TypeScript and Sass are located in the [src](src) directory.

### Setup

Requires [Node.js](https://nodejs.org/en).

To install dev packages:

```console
$ npm install
```

### Build assets

To compile the [src](src) files into the `.js` and `.css` bundles loaded by Django:
```console
$ gulp
```

To watch [src](src) files and build continuously (useful to run alongside
`manage.py runserver` during development):
```console
$ gulp watch
```

### Write and run unit tests

TypeScript unit tests are located in the [tests_js](tests_js) directory.

To run unit tests using [Mocha](https://mochajs.org/):

```console
$ npm test
```

### Linting

To lint TypeScript code using [ESLint](https://eslint.org/):

```console
$ npm run lint
```
