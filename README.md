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
│   ├── backend
│   │   ├── deploy_script.sh
│   │   ├── Django
│   │   ├── Dockerfile
│   │   ├── __init__.py
│   │   └── requirements.txt
│   ├── frontend
│   │   └── Dockerfile
│   ├── __init__.py
│   ├── nginx
│   │   └── nginx.conf
│   ├── Readme.md
│   ├── survey_form
│   │   ├── db.sqlite3
│   │   ├── Dockerfile
│   │   ├── manage.py
│   │   ├── requirements.txt
│   │   ├── survey_app
│   │   ├── survey_form_backend
│   │   ├── survey_frontend
│   │   ├── surveys
│   │   └── venv
│   └── test_github_access.txt
├── demo
│   ├── CS673_presentation0_team3
│   └── Readme.md
├── doc
│   ├── CS673_MeetingMinutes_team3.docx
│   ├── CS673_presentation0_team3.pptx
│   ├── CS673_ProgressReport_team3.xlsx
│   ├── CS673_SDD_team3.docx
│   ├── CS673_SPPP_RiskManagement.xlsx
│   ├── CS673_SPPP_team3.docx
│   ├── CS673_STD_team3.docx
│   ├── ProjectDescription.docx
│   ├── pull_request_template.md
│   └── Readme.md
├── misc
│   └── Readme.md
├── README.md
├── team.md
└── venv
    ├── bin
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── Activate.ps1
    │   ├── django-admin
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.10
    │   ├── python -> /home/murosev/anaconda3/bin/python
    │   ├── python3 -> python
    │   ├── python3.10 -> python
    │   └── sqlformat
    ├── include
    ├── lib
    │   └── python3.10
    ├── lib64 -> lib
    └── pyvenv.cfg

21 directories, 41 files

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
