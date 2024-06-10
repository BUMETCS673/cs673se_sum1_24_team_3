# Rhettoric

## About
Rhettoric is a project focused on creating a survey. The project aims to provide accurate and reliable insight to a user's experience and feedback on a given course.
## Overview
This is a project for the CS 673 class with Dr. Zhang. The objective is to create a survey for a course learning platform where at the end of the course, a survey is generated and distributed to the users to answer and provide valuable feedback to the course creator. 
Related Work
Blackboard: A widely used learning management system (LMS) that offers course management, customizable open architecture, and scalable design.
Coursera: An online learning platform that provides courses, specializations, and degrees.
Udemy: An online learning and teaching marketplace.

This document explains the structure of the GitHub repository along with contents of files. This will mirror the Github repository and can be used here as a sort of “Staging” environment until we are ready to move the “Non-Code Related” files to Github. CODE should still be stored in Github and worked on in realtime there not here. Google Drive documents will be uploaded to GitHub at the end of every iteration or after major changes. 

## Structure of this Project is as follows:
```
.
├── code
│   ├── local_testing_adrian_dnu
│   │   ├── myapp
│   ├──  ├── migrations
│   │     └── .DS_Store
│   │     └── 0001_initial.py
│   │     └── __init__.py
│   ├──  ├── static/js
│   │     └── login.js
│   │     └── register.js
│   ├──  ├── templates
│   │     └── home.html
│   │     └── login.html
│   │     └── register.html
│   ├──  ├── __init__.py
│   ├──  ├── admin.py
│   ├──  ├── apps.py
│   ├──  ├── forms.py
│   ├──  ├── models.py
│   ├──  ├── tests.py
│   ├──  ├── urls.py
│   ├──  ├── views.py
│   │   ├── myproject
│   │     └── __init.py__
│   │     └── settings.py
│   │     └── urls.py
│   │     └── wsgi.py
│   │   ├── db.sqlite3
│   │   ├── docker-compose.yml
│   │   ├── Dockerfile
│   │   ├── manage.py
│   │   ├── requirements.txt
│   │   ├── Testing_Instructions_Local.txt
│   ├── survey_form
│   │   ├── survey_app
│   ├──  ├── migrations
│   │     └── 0001_initial.py
│   │     └── __init__.py
│   ├──  ├── __init__.py
│   ├──  ├── admin.py
│   ├──  ├── apps.py
│   ├──  ├── models.py
│   ├──  ├── runtests.py
│   ├──  ├── serializers.py
│   ├──  ├── tests.py
│   ├──  ├── urls.py
│   ├──  ├── views.py
│   │   ├── survey_form_backend
│   ├──  ├── backend
│   ├──   ├── Django
│   ├──    ├── Settings
│   ├──     ├── nginx
│   │        └── nginx.conf
│   ├──     ├── __init__.py
│   ├──     ├── base_settings.py
│   ├──     ├── production_settings.py
│   ├──     ├── staging_settings.py
│   ├──     ├── test_settings.py
│   ├──    ├── __init__.py
│   │      └── manage.py
│   │      └── __init__.py
│   │     └── Dockerfile
│   │     └── __init__.py
│   │     └── requirements.txt
│   ├──  ├── __init__.py
│   ├──  ├── asgi.py
│   ├──  ├── settings.py
│   ├──  ├── urls
│   ├──  ├── wsgi.py
│   │   ├── survey_frontend
│   │   ├── surveys
│   ├──  ├── migrations
│   │     └── __init__.py
│   ├──  ├── __init__.py
│   ├──  ├── admin.py
│   ├──  ├── apps.py
│   ├──  ├── models.py
│   ├──  ├── serializers.py
│   ├──  ├── tests.py
│   │   ├── .gitignore
│   │   ├── Dockerfile
│   │   ├── __init__.py
│   │   ├── manage.py
│   │   ├── requirements.txt
│   ├── Readme.md
│   ├── __init__.py
│   ├── test_github_access.txt
├── demo
│   ├── CS673_presentation0_team3
│   └── Readme.md
├── doc
│   ├── CS673_MeetingMinutes_team3.docx
│   ├── CS673_presentation0_team3.pptx
│   ├── CS673_ProgressReport_team3.xlsx
│   ├── CS673_SDD_team3.docx
│   ├── CS673_SPPP_RiskManagement.xlsx
│   ├── CS673_SPPP_team3.docx
│   ├── CS673_STD_team3.docx
│   ├── DB_old.png
│   ├── DB_updated.png
│   ├── exam.drawio
│   ├── meeting_minutes
│   ├── ProjectDescription.docx
│   ├── Readme.md
├── Iteration
│   ├──  ├── iteration1
│   │       └── CS673_iteration1demo_team3 (video)
│   │       └── CS673_presentation1_teamX
│   │       └── readme.md
│   ├──  ├── iteration2
│   │       └── CS673_iteration2demo_team3_video //TODO
│   │       └── CS673_presentation2_team3
│   │       └── readme.md
├── misc
│   └── Readme.md
├── .gitignore
├── __init__.py
├── README.md
├── team.md


```

```
code
“This folder contains all source code and test code.” (Completed files preferably) 
demo
	“This folder contains all demo videos”
doc
	“This folder contains all required documents, including SPPP, SDD, STD, meetingminutes and progressreport”
misc
	“This folder contains any additional information about the project.”

```
