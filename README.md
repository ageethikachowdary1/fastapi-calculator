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

```
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
```

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


## Reflection

During this assignment, I learned how to build a web application using FastAPI and test it using unit, integration, and end-to-end testing. I also gained experience in implementing logging and setting up continuous integration using GitHub Actions. This helped me understand how to develop, test, and automate Python-based web applications.


## Module 9: Docker + PostgreSQL + pgAdmin Integration

This project was extended using Docker Compose to include PostgreSQL and pgAdmin for database management.

### Features Added

- Dockerized FastAPI, PostgreSQL, and pgAdmin services  
- Created database tables using SQL  
- Inserted, queried, updated, and deleted data  
- Implemented one-to-many relationship using foreign keys  
- Executed queries using pgAdmin  

### Docker Setup

The application was started using:

docker compose up --build

pgAdmin was accessed at:

http://localhost:5050

### Database Operations

The following SQL operations were performed:

- CREATE TABLE (users, calculations)  
- INSERT INTO (added sample records)  
- SELECT (retrieved data)  
- JOIN (combined users and calculations)  
- UPDATE (modified existing record)  
- DELETE (removed a record)  

### Outcome

This module demonstrates how a FastAPI application can be integrated with a PostgreSQL database using Docker, and how SQL is used to manage relational data.
