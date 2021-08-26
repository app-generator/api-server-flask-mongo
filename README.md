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

> **[Free Version](https://github.com/app-generator/api-server-flask)** available: SQLite persistance, Unitary Tests, 24/7 LIVE Support via [Discord](https://discord.gg/fZC6hup)

> Can be used with other [React Starters](https://appseed.us/apps/react) for a complete **Full-Stack** experience:

| [React Node JS Berry](https://appseed.us/product/react-node-js-berry-dashboard) | [Full-Stack Material PRO](https://appseed.us/full-stack/react-material-dashboard) | [React Node Datta Able](https://github.com/app-generator/react-datta-able) |
| --- | --- | --- |
| [![React Node JS Berry](https://user-images.githubusercontent.com/51070104/124934742-aa392300-e00d-11eb-83bf-28d8b8704ec8.png)](https://appseed.us/product/react-node-js-berry-dashboard) | [![Full-Stack Material PRO](https://user-images.githubusercontent.com/51070104/128878037-50da7a12-787d-455d-933a-30b2957e2896.png)](https://appseed.us/full-stack/react-material-dashboard) | [![React Node Datta Able](https://user-images.githubusercontent.com/51070104/125737710-834a9e6f-c39b-4f3b-a42a-9583ce2ce1da.png)](https://github.com/app-generator/react-datta-able)

<br />

![Flask API Server - Open-source Flask Starter provided by AppSeed.](https://user-images.githubusercontent.com/51070104/126349643-264d4cf4-6d0b-4c24-8185-adf69409fa4e.png)

<br />

## Table of Contents

1. [Getting Started](#getting-started)
2. [Project Structure](#project-structure)
3. [Modules](#modules)
4. [Testing](#testing)


## Getting Started

**Step #1** - clone the project (private repository)

```bash
$ git clone https://github.com/app-generator/priv-api-server-flask-pro.git
$ cd priv-api-server-flask-pro
```

**Step #2** - create virtual environment using python3 and activate it (keep it outside our project directory)

```bash
$ python3 -m venv /path/to/your/virtual/environment
$ source <path/to/venv>/bin/activate
```

**Step #3** - install dependencies in virtualenv

```bash
$ pip install -r requirements.txt
```

**Step #4** - setup `flask` command for our app

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

**Step #5** - start test APIs server at `localhost:5000`

```bash
$ python run.py
```
or 
```bash
$ flask run
```

**Step #6** - use `flask-restx`' swagger dashboard to test APIs, or use `POSTMAN`

<br />

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

<br />

## Testing

Run tests using `pytest tests.py`

<br />

---
**Flask API Server PRO** - provided by AppSeed [App Generator](https://appseed.us)
