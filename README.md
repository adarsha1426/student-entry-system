# Student Entry System - Django Task

## Introduction

This is a Django-based student entry system with integration of Django Rest Framework (DRF). The system allows an admin to:

- Record new student details
- Update student details
- Delete student records

The application runs on `localhost` at port `8025`.

## Features

- Web-based UI for student management (using Django Forms or simple HTML forms)
- REST API for CRUD operations
- Uses Virtualenv or Pipenv for environment management
- Follows clean code practices with proper naming conventions

## Model Description

### Model: `Student`

| Field   | Data Type |
| ------- | --------- |
| Name    | String    |
| Age     | Integer   |
| Address | String    |
| Grade   | String    |
| Major   | String    |

## Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/adarsha1426/student-entry-system
   cd StudentEntrySystem
2. **Create the Virtual Environment**
   ```bash
   python -m venv <env-name>
   <env-name>\Scripts\activate
3. **Install the requirements**
   ```bash
   pip install -r requirements.txt
4. **Run the project**
   ```bash
   cd StudentEntrySystem
   python manage.py runserver 8025
5 **Browse on the web**
  http://127.0.0.1:8025
   

