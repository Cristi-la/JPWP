# Crab - Compact Rest API backend

Crab is a Python package for building web applications. It provides a lightweight framework for handling HTTP requests and responses, routing URL paths to views, and managing application settings.

## Features

- HTTP request and response handling
- JSON, XML, HTML header handling
- URL routing to views
- Application settings management

## Installation

You can install Crab using pip:

```bash
python3 ./setup.py sdist
pip3 install ./crab/dist/crab-1.0.0.tar.gz
```

## Inicialization

```bash
crab --create
```

## Features

- Lightweight and easy-to-use
- Supports HTTP requests
- Modular architecture
- Customizable response headers
- Error handling and logging

## How it works

1. Install package
2. Configure application settings in `settings.py`.
3. Create function view in `views.py`
4. Register view in url `urls.py` to str path or regex path.
5. Start web service:

```
python3 deal.py
```
