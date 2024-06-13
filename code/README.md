The is implemented using a Django webserver and sqlite database. The code can either be ran locally in a python virtual environent or within the Docker engine using the included Dockerfile and docker-compose.yml

To run locally:

1) create a python virtual environment

`python -m venv env`

2) ACtivate the python virtual environemnt

Windows
`.\env\Scripts\activate`

3) Install dependencies list

`pip install -r requirements.txt`

4) Run django webserver

`python manage.py runserver`

5) Browse to http://localhost:8000


To run in Docker

Run `docker-compose up`

Browse to https://127.0.0.1:8000

## Code Structure
```
└── 📁code
    └── .dockerignore
    └── docker-compose.yml
    └── Dockerfile
        └── manage.py
        └── requirements.txt
        └── 📁surveys
            └── admin.py
            └── apps.py
            └── models.py
            └── runtests.py
            └── serializers.py
            └── tests.py
            └── urls.py
            └── views.py
            └── __init__.py
        └── 📁survey_app
            └── .env
            └── asgi.py
            └── settings.py
            └── urls.py
            └── wsgi.py
            └── __init__.py
        └── 📁users
            └── admin.py
            └── apps.py
            └── forms.py
            └── models.py
            └── 📁static
                └── 📁js
                    └── login.js
                    └── register.js
            └── 📁templates
                └── home.html
                └── login.html
                └── register.html
            └── tests.py
            └── urls.py
            └── views.py
            └── __init__.py
```

