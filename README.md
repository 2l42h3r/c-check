# ccheck

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=2l42h3r_c-check&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=2l42h3r_c-check)

Tool for generating and checking simple C language exercises.

## Requirements
* at least Python 3.7
* Pip installed

## Running from source without building

Install dependencies:

```bash python -m pip -r requirements.txt```

Add project to PYTHONPATH (this depends on OS)

Run project as module:

```bash python -m src.ccheck```

## Build from source

Install dependencies:

```bash python -m pip -r requirements.txt```

Install/update build tools:

```bash python -m pip install --upgrade build```

Build:

```bash python -m build```


Files will be outputted to dist/

## Install local package build

```bash python -m pip install dist/ccheck_2l42h3r-VERSION-*.whl```