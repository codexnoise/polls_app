# Polls Web App
This web app for add questions and choices.

## Tech Stack

Developed with Python, Django, Html and SQLite

## Installation

Clone or download the repository:  
`https://github.com/noisecodex/polls_app.git`

Go to the project directory:  
`cd polls_app`

Create a virtual environment (PowerShell):  
` python -m venv venv`  
`.\venv\Scripts\activate`

Install dependencies:  
`pip install -r requirements.txt`

Make migrations for the database:  
`py manage.py makemigrations polls`  
`py manage.py migration`

Create a super user to access the django´s administration panel and add the questions and choices for the app. Remember that each question should have at least two choices.  
`py manage.py createsuperuser`

Run the app:  
`py manage.py runserver`

## Contributing
Contributions are always welcome!

Fork this repository;

Create a branch with your feature:  
`git checkout -b my-feature`

Commit your changes:  
`git commit -m "feat: my new feature"`

Push to your branch:  
`git push origin my-feature `

## Author
@noisecodex

## License
This project is under MIT License.
