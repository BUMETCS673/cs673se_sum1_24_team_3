This folder is the Django API that allowisng superuser to create and modify and deleting the surveys.
The testing process is like following:
1) create a python virtual environment

`python -m venv env`

2) ACtivate the python virtual environemnt

Windows
`.\env\Scripts\activate`

3) Install dependencies list

`pip install -r requirements.txt`

4) Run django testing

`python manage.py test surveys.tests`
`python manage.py test surveys.tests_api`

Or adding, modifing, and deleting the surveys by Django API:

1) create a python virtual environment

`python -m venv env`

2) ACtivate the python virtual environemnt

Windows
`.\env\Scripts\activate`

3) Install dependencies list

`pip install -r requirements.txt`

4) Run django testing

`python manage.py runserver`

5) accessing the API by browsing to [127.0.0.1:8000/api/](http://127.0.0.1:8000/api/surveys/) for survey
http://127.0.0.1:8000/api/questions/ for questions
http://127.0.0.1:8000/api/responses/ for respondses
