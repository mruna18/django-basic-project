# Django Basic Project

This is a simple Django project created as part of my learning journey. The main purpose of this project is to practice Django's basic concepts, such as setting up a project, managing views and templates, and handling static files.

## Features
✔ Simple webpage structure with Django templates  
✔ URL routing for different pages (Home, About)  
✔ Static file handling (CSS, images)  
✔ Basic project setup using Django  

## Installation and Setup

To run this project on your local machine, follow these steps:

### 1. Clone the Repository
```sh
git clone https://github.com/mruna18/django-basic-project.git
cd django-basic-project

### 2. Create a Virtual Envirnoment
``` sh
python -m venv myenv
Activate the virtual evirnoment in 
a. Windows : venv\Scripts\activate
b. Mac/Linux : source venv/bin/activate

### 3. Install the dependencies
```sh
pip install django

### 4. make project
```sh
django-admin startproject myproject

### 5. change directory to myproject and open it in vscode
cd myproject
code .

### 6. in vs code open cmd and start the django development server
```sh
python manage.py runserver