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
│   ├── survey_app
│   │   ├── survey_app
│   ├──  ├── __init__.py
│   ├──  ├── asgi.py
│   ├──  ├── settings.py
│   ├──  ├── urls
│   ├──  ├── wsgi.py
│   │   ├── surveys
│   ├──  ├── migrations
│   │     └── 0001_initial.py
│   │     └── 0002_remove_question_choice_type_remove_response_question_and_more.py
│   │     └── 0003_alter_survey_description.py
│   │     └── 0004_response_question.py
│   │     └── 0005_alter_response_question.py
│   │     └── 0006_remove_response_question.py
│   │     └── 0007_response_question.py
│   │     └── 0008_alter_question_text_alter_survey_title.py
│   │     └── __init__.py
│   ├──  ├── __init__.py
│   ├──  ├── admin.py
│   ├──  ├── apps.py
│   ├──  ├── models.py
│   ├──  ├── permissions.py
│   ├──  ├── README.md
│   ├──  ├── runtests.py
│   ├──  ├── serializers.py
│   ├──  ├── tests.py
│   ├──  ├── tests_api.py
│   ├──  ├── urls.py
│   ├──  ├── views.py
│   │   ├── users
│   ├──  ├── migrations
│   │       └── 0001_initial.py
│   │       └── __init__.py
│   │   ├── static
│   ├──  ├── js
│   │     └── login.js
│   │     └── register.js
│   ├──  ├── templates
│   │       └── dashboard.html
│   │       └── home.html
│   │       └── login.html
│   │       └── register.html
│   │       └── take_survey.html
│   │       └── view_survey.html
│   ├──  ├── __init__.py
│   ├──  ├── admin.py
│   ├──  ├── apps.py
│   ├──  ├── forms.py
│   ├──  ├── models.py
│   ├──  ├── README.md
│   ├──  ├── tests.py
│   ├──  ├── tests_selenium.py
│   ├──  ├── urls.py
│   ├──  ├── views.py
│   │   ├── manage.py
│   │   ├── requirements.txt
│   ├── .dockerignore
│   ├── docker-compose.yml
│   ├── Dockerfile.app
│   ├── Dockerfile.test
│   ├── README.md
├── demo
│   └── Readme.md
├── doc
│   ├── CS673_MeetingMinutes_team3.docx
│   ├── CS673_ProgressReport_team3.xlsx
│   ├── CS673_SDD_team3.docx
│   ├── CS673_SPPP_RiskManagement.xlsx
│   ├── CS673_SPPP_team3.docx
│   ├── CS673_STD_team3.docx
│   ├── DB_updated.png
│   ├── exam.drawio
│   ├── ProjectDescription.docx
│   ├── pull_request_template.md
│   ├── Readme.md
├── iteration
│   ├──  ├── iteration0
│   │       └── CS673_presentation0_team3
│   │       └── CS673_presentation0_team3.pptx
│   │       └── Iteration 0 Team 3.pptx
│   ├──  ├── iteration1
│   │       └── CS673_iteration1demo_team3 (video)
│   │       └── CS673_presentation1_teamX
│   │       └── readme.md
│   ├──  ├── iteration2
│   │       └── CS673_presentation2_team3.pptx
│   │       └── README.md
│   │       └── Team3_Rhetoric_Iteration2_Presentation.mp4
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
