# {{ project_name }}

## Installation

### Create and activate a Python virtual environment
On Linux/macOS with bash/zsh:
```console
$ python -m venv venv
$ source venv/bin/activate
```

For the same commands on different platforms and shells, see the
[documentation for venv](https://docs.python.org/3/library/venv.html#creating-virtual-environments).

### Install packages
```console
$ pip install --upgrade pip
$ pip install -r requirements.txt
```

### Run test server
```console
$ python manage.py runserver
...
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

View the website in your browser at [127.0.0.1:8000](http://127.0.0.1:8000/).

## Development

### Python

#### Install packages
```console
$ pip install -r requirements-test.txt
```

#### Apply formatting
To apply black and isort formatting:
```console
$ black .
$ ruff check --select I --fix .
```

#### Type checking
```console
$ mypy
```

#### Linting
```console
$ ruff check .
```

#### Run unit tests
To run unit tests and report coverage to terminal:
```console
$ pytest --cov-report=term
```

### TypeScript / SASS

Requires [Node.js](https://nodejs.org/en). Source files for both TypeScript and SASS
are located in [/src](src).

#### Install packages
```console
$ npm install
```

#### Build
To build the JS and CSS assets loaded in the base template:
```console
$ gulp
```

To watch files and build continuously (useful to run alongside `manage.py runserver`):
```console
$ gulp watch
```

#### Linting
```console
$ npm run lint
```

#### Run unit tests
```console
$ npm test
```
