This folder is the Django API that allowisng superuser to create and modify and deleting the surveys.
The testing process is like following:

1) Run django testing

`python manage.py test surveys.tests`
`python manage.py test surveys.tests_api`

Or adding, modifing, and deleting the surveys by Django API:

1) Run django development server

`python manage.py runserver`

2) Access the API by browsing to [127.0.0.1:8000/api/](http://127.0.0.1:8000/api/surveys/) for survey
http://127.0.0.1:8000/api/questions/ for questions
http://127.0.0.1:8000/api/responses/ for responses
