# THIS APP

## Index
- [Design](#design)  
- [Tools](#tools)
    - [Views](#views)
    - [Serializers](#serializers)
    - [CRUD](#crud)
    - [Frontend](#frontend)
- [Deployment](#deployment)
    - [Creating Admin](#creating-admin)
- [API](#api)
    - [Installing requests](#installing-requests)
    - [Using requests](#using-requests)
- [Alternatives](#alternatives)
    - [WSGI vs ASGI](#wsgi-vs-asgi)
    - [Pyenv and Virutal Env Manager](#pyenv-and-virutal-env-manager)
    - [ORM](#orm)
- [Troubleshoot](#troubleshoot)

## Design
###### ref: Domain Driven Design: https://martinfowler.com/tags/domain%20driven%20design.html
The project contains three apps:
- department
- demployee
- home

Each one holds its own migrations, models and views for both the webpages and API. However, the `home` app does not count on an API given that is serves as a "mounting point" for all the other apps by making the project point to it as the home page which then points to the other domains.

The project itself was designed to respect the DDD (Domain Driven Design) that is the reason of using different apps for each context of department and student. It may be a possibility (or even a better practice) to have the APIs as separated apps (or maybe "sub-apps" of the entity).

## Tools

### Views
It uses `APIView` for the view layer in rest framework. It was choosen because of the better organised form of each HTTP verb being a class method along with the possibility to authenticate the endpoints by simpling implementing an auth property.

It also uses `ModelViewSet` but for the webpage renderization. It was a possibility to use the API itself and all the endpoints that the previous paragraph mentioned, but using a different type of model is a good learning approach.

### Serializers
The serializer we are using is the `ModelSerializer`. All classes for all entities are using this class and displaying all the data available in the API. Given that there is no internal-only information such as a sensitive information (document, etc.) or an unique id for API control (and therefore not useful for the web customer) there was no need to implement any kind of form layer (altough I'd love to test it if I had more time).

### CRUD
The project uses the Django manner of CRUD/ORM by treating the object model itself. We could also have used tools such as Flask+SQLAlchemy for this layer for better CRUD control or even implement the Unit of Work design pattern.

### Frontend
For templates the project uses both django notation for objects and html + javascript. They are very simple, just to show the application's features of listing the departments and employees. All the CRUD can be done using the `/admin` endpoint. It will be detailed later below in `Deployment` section.


## Deployment

Clone the project to your machine:
```bash
git clone https://github.com/paulo-rodrigues021/this_app.git
```

Create the virtual env:
```bash
python -m venv venv
```

Activate it:
```bash
source venv/bin/activate
```

Install the requirements:
```bash
pip install -r requirements.txt
```

Prepare the migrations:
```bash
python manage.py makemigrations
```

Run the migrations:
```bash
python manage.py migrate
```

Run application:
```bash
python manage.py runserver
```

Now the application is working in the default port `8000`. You may access it by opening a browser and entering the url `http://127.0.0.1:8000`

### Creating Admin

Create a superuser to serve as an admin:
```bash
python manage.py createsuperuser
```

Define the username:
```bash
Username: jane doe
```

Enter the email address:
```bash
Email address: jane.doe@example.com
```

Then enter the password twice:
```bash
Password: ******
Password(again): ******
```

Now you have access to the application's `admin` endpoint. You may access it in `http://127.0.0.1:8000/admin/`


## API

### Installing requests
###### ref: https://pypi.org/project/requests/

To use the API make sure the application is running (you may follow the previous steps right above this section). Once you do, one very popular way to use an API in python is by the `requests` lib. Open up a new terminal, initiate a virtualenv and do the following:

Install `requests`:
```bash
pip install requests
```

### Using requests
Start a python interactive shell by entering `python3` in the terminal:
```bash
python3
```

Make an API call:
```py
import requests

base_url = "http://127.0.0.1:8000/api"

# Creating department
response = requests.post(url = base_url + "/department/", data={"name": "mathematics"})

# Checking response
response.status_code
>>> 201

# Getting the object
response = requests.get(url = base_url + "/department/")

# Checking response
response.status_code
>>> 200

# Showing the objects
response.json()
>>> ['mathematics']

# Deleting it
# Note: Ideally it would be done by a path parameter not a query parameter.
response = requests.delete(url = url + "/department?name=mathematics")

# Checking
response.status_code
>>> 204
```

The example was done using the `department` object, but all CRUD options are available for employee too. You may access both API's documentation in `http://127.0.0.1:8000/api/department/` and `http://127.0.0.1:8000/api/employee/`.

When using the employee API, remember to first create the department register before creating an employee for it. Also, the `department` named field value that will be passed in POST body should refer to the department's id, not its name.

## Alternatives
These are a few alternatives for some layers in this project. Ideally I'd write different versions of this app using different tools just for the curiosity matter. I think it is good for at least mention each one.

### WSGI vs ASGI
###### ref: https://fastapi.tiangolo.com/
While Django uses WSGI, there are different web frameworks that use ASGI as is the case for FastAPI. FastAPI may be used to develop API layer inside a Django project. It takes the advantage of using ASGI which is way faster and ready for production scalability due to its asynchronous nature. It can also render HTML templates which may serve the webpages for both API routes and web server.

### Pyenv and Virutal Env Manager
###### ref: https://python-poetry.org/
###### ref: https://realpython.com/intro-to-pyenv/
With the intetion to replace the normal `venv` framework to manager virtual envs in python, the `poetry` tool is very useful. It makes it a lot easier to control release versions of the project, separate the production libs from the dev ones, etc. 

Along with it, `pyenv` is a very powerful python version control. It allows you to have multiple python versions in your machine and use a different one in each project by using simple commands such as `pyenv local 3.9.10` to set a local python version for a project and `pyenv global 3.11` for the machine entirely.

Using both in a project makes it a lot easier to control dependences in a production scenario.

### ORM
###### ref: https://www.sqlalchemy.org/
SQLAlchemy is a great ORM tool for python and it works with different databases such as MariaDB, MySQL, Postgres, etc. It create queries using python object notation and can be used together with Flask (that is an alternative for FastAPI also) and FastAPI inside of a Django project.

AQLAlchemy also helps to control object's idepotency by controlling its CRUD options by using different sessions. It is very helpful in a distributed environment.

## Troubleshoot
Depending on your machine's python version, it may be necessary to change the python version required for the project. There are a few ways to do it:
1. Install a different python version in your machine that will serve the project
2. Install `pyenv` framework. You may use it to download all the python versions you need and define a local python version that is required in this project.
