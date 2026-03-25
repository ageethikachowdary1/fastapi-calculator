# FastAPI Calculator Web Application

## Overview

This project is a web-based calculator built using FastAPI.
It demonstrates REST API development, testing, logging, and continuous integration using GitHub Actions.

The application allows users to perform basic arithmetic operations through a web interface.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Error handling (division by zero)
- Logging of operations and errors
- Web-based user interface

## Technologies Used

- Python 3.12
- FastAPI
- Uvicorn
- Pytest
- Playwright (End-to-End Testing)
- Git
- GitHub Actions

## Project Structure

fastapi-calculator/
|-- main.py
|-- operations.py
|-- templates/
|   |-- index.html
|-- tests/
|   |-- test_operations.py
|   |-- test_main.py
|   |-- test_e2e.py
|-- .github/workflows/ci.yml
|-- requirements.txt
|-- pytest.ini
|-- .gitignore
|-- README.md

## Running the Application

Activate virtual environment and run:

uvicorn main:app --reload

Open in browser:
http://127.0.0.1:8000

## Running Tests

Unit and Integration:

pytest tests/test_operations.py tests/test_main.py -v

End-to-End:

pytest tests/test_e2e.py -v

## Logging

The application logs:
- calculation requests
- errors like invalid operations or division by zero

## Continuous Integration

GitHub Actions automatically:
- installs dependencies
- runs tests
- starts FastAPI server
- runs Playwright tests

All tests must pass.

## Learning Outcomes

- REST API development using FastAPI
- Unit and integration testing
- End-to-end testing with Playwright
- Logging implementation
- Git and GitHub usage
- CI/CD using GitHub Actions

## Status

- Application working
- All tests passing
- CI successful
