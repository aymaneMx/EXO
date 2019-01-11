# EXO
Django application with ajax modal popup

## Introduction 
It is a small app that does the following instructions:
* a page allowing a user to log in.
* Once logged in, the user accesses the page displaying his profile and changes (first name /last name/email).
* By clicking on "Edit information", a modal open up.
* In this modal, an input to modify his first name, last name and email address, as well as a "save" button. In support of this button, the information will be modified in the database and on the main page without reloading the page.

## Screenshots
![alt text](https://github.com/aymaneMx/EXO/blob/master/assets/example-gif.gif)

## Quick start
1. Clone repo like this:
	`git clone  https://github.com/aymaneMx/EXO.git`

2. Create a virtualenv:
	`python -m venv virtualenv`
3. Activate virtualenv
4. Install packages from requirements.txt file
5. Run python manage.py migrate
6. Start the development server and visit http://127.0.0.1:8000/todo/
