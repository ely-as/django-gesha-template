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

## Development

### Install packages
```console
$ pip install -r requirements-test.txt
```

### Apply formatting
To apply black and isort formatting:
```console
$ black .
$ ruff check --select I --fix .
```

### Type checking
```console
$ mypy
```

### Linting
```console
$ ruff check .
```

### Run unit tests
To run unit tests and report coverage to terminal:
```console
$ pytest --cov-report=term
```
