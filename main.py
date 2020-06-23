'''flask installation (CMD):
python -m venv env
env\Scripts\activate
pip install Flask
deactivate


We create the main catalog application, just next to the catalog with virtual
environment. It will gather the logic of our app, all functions, templates,
styles etc.
It is also recommended to create the tests catalog at the same level, in 
future we will place there a file with unit tests.
In this catalog we will find following folders and files:
Folder static – with static files (styles, pics, icons, scripts in JavaScript)
Folder templates – with page layout in HTML, main page and subpages
File main.py – main app logic that links all components which are necessary 
to run an application
File scripts.py – in here we will define the functions that will serve the app
and transfer the data to main.py
To sum up, the structure of our application will look as follows:
application
|—- static
|—- templates
|—– main.py
|—– scripts.py
env
tests'''

#imports - importing flask library with class Flask for our app
from flask import Flask

#application variable - assigning Flask to variable app where an instance
#of class Flask is created
app = Flask(__name__)

#routing - decorator pattern @app.route(‚/’) says that while running
#an appropriate url in borowser, function below should be executed. 
#For the main webpage url  = ‚/’, i.e. for blog it would be url = ‚/blog’ etc.

@app.route('/')
def hello_world():
    return '<h1>A pug is cute and chubby</h1>'

#debug - interesting example: conditional thanks to which we will not have
#to run the app from virtual environment each time when a change is made:
#debug mode is switched on
if __name__ == '__main__':
    app.run(debug=True)