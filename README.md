## [Flask API Server - Mongo](https://github.com/app-generator/api-server-flask-mongo)

Flask Starter with JWT authentication, and **SQLite** persistance - Provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
It has all the ready-to-use bare minimum essentials.

<br />

> Features:

- ✅ `Up-to-date dependencies` 
- ✅ [API Definition](https://docs.appseed.us/boilerplate-code/api-unified-definition) - the unified API structure implemented by this server
- ✅ Simple JWT API powered by `flask-restx` and `flask_jwt_extended`
- ✅ Authentication with JWT (JWT login, JWT logout, Register)
- ✅ **Persistance**:  `MongoDB`
- ✅ Unitary tests, Docker

<br />

> Can be used with other [React Starters](https://appseed.us/apps/react) for a complete **Full-Stack** experience:

| [React Node JS Berry](https://appseed.us/product/berry-dashboard/api-server-nodejs/react/) | [React Node Soft Dashboard](https://appseed.us/product/soft-ui-dashboard/api-server-nodejs/react/) | [React Node Horizon](https://appseed.us/product/horizon-ui/api-server-nodejs/) |
| --- | --- | --- |
| [![React Node JS Berry](https://user-images.githubusercontent.com/51070104/176936514-f1bccb21-bafe-4b43-9e4c-b6fe0ec9511d.png)](https://appseed.us/product/berry-dashboard/api-server-nodejs/react/) | [![React Node Soft Dashboard](https://user-images.githubusercontent.com/51070104/176936814-74386559-4e05-43d5-b9a4-8f70ce96a610.png)](https://appseed.us/product/soft-ui-dashboard/api-server-nodejs/react/) | [![React Node Horizon](https://user-images.githubusercontent.com/51070104/174428337-181e6dea-0ad9-4fe1-a35f-25e5fa656a9d.png)](https://appseed.us/product/horizon-ui/api-server-nodejs/)

<br />

![Flask API Server - Open-source Flask Starter provided by AppSeed.](https://user-images.githubusercontent.com/51070104/126349643-264d4cf4-6d0b-4c24-8185-adf69409fa4e.png)

<br />

## Table of Contents

1. [Getting Started](#getting-started)
2. [Project Structure](#project-structure)
3. [Modules](#modules)
4. [Testing](#testing)


## Getting Started

clone the project

```bash
$ git clone https://github.com/app-generator/api-server-flask-mongo.git
$ cd api-server-flask-mongo
```

create virtual environment using python3 and activate it (keep it outside our project directory)

```bash
$ python3 -m venv /path/to/your/virtual/environment
$ source <path/to/venv>/bin/activate
```

install dependencies in virtualenv

```bash
$ pip install -r requirements.txt
```

setup `flask` command for our app

```bash
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
```

> Or for Windows-based systems

```powershell
$ (Windows CMD) set FLASK_APP=run.py
$ (Windows CMD) set FLASK_ENV=development
$
$ (Powershell) $env:FLASK_APP = ".\run.py"
$ (Powershell) $env:FLASK_ENV = "development"
```

start test APIs server at `localhost:5000`

```bash
$ python run.py
```
or 
```bash
$ flask run
```

use `flask-restx`' swagger dashboard to test APIs, or use `POSTMAN`


## Project Structure

```bash
api-server-flask/
├── api
│   ├── config.py
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── Dockerfile
├── README.md
├── requirements.txt
├── run.py
└── tests.py
```

<br />

## Docker

Our docker image details are in `Dockerfile`

To build the docker image (replace app name between `< >` as per your requirment)

```bash
$ docker build -t <api-server-flask-app>:latest .
```

To run the docker container

```bash
$ docker run -d -p 5000:5000 <api-server-flask-app>
```

<br />

## Modules

This application uses the following modules

 - Flask==1.1.4
 - flask-restx==0.4.0
 - Flask-JWT-Extended
 - flask-mongoengine
 - pytest

## Testing

Run tests using `pytest tests.py`

<br />

---
[Flask API Server - Mongo](https://github.com/app-generator/api-server-flask-mongo) - provided by AppSeed [App Generator](https://appseed.us)
