## Flask API Server PRO

Flask Starter with JWT authentication, and **SQLite** persistance - Provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
It has all the ready-to-use bare minimum essentials.

<br />

> Features:

- [API Definition](https://docs.appseed.us/boilerplate-code/api-unified-definition) - the unified API structure implemented by this server
- Simple JWT API powered by `flask-restx` and `flask_jwt_extended`
- Authentication with JWT (JWT login, JWT logout, Register)
- Branches:
    - **Master**: SQLite Persistence
    - **Mongo**:  MongoDB Persistence
- Unitary tests, Docker

<br />

> Can be used with other UI projects for a complete **fullstack** experience  

- [React Berry Dashboard](https://github.com/app-generator/react-berry-admin-template) - open-source sample
- [React Datta Dashboard](https://github.com/app-generator/react-datta-able-dashboard) - open-source sample
- [React Datta Dashboard PRO](https://appseed.us/product/react-node-js-datta-able-pro) - commercial fullstack product

<br />

> Support: 

- Github (issues tracker), Email: **support @ appseed.us** 
- **Discord**: [LIVE Support](https://discord.gg/fZC6hup) (registered AppSeed Users) 

<br />

![Flask API Server - Open-source Flask Starter provided by AppSeed.](https://user-images.githubusercontent.com/51070104/126349643-264d4cf4-6d0b-4c24-8185-adf69409fa4e.png)

<br />

## Table of Contents

1. [Getting Started](#getting-started)
2. [Project Structure](#project-structure)
3. [Modules](#modules)
4. [Testing](#testing)


## Getting Started

clone the project (private repository)

```bash
$ git clone https://github.com/app-generator/priv-api-server-flask-pro.git
$ cd priv-api-server-flask-pro
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
 - pytest

## Testing

Run tests using `pytest tests.py`

<br />

---
Flask API Server - provided by AppSeed [App Generator](https://appseed.us)
