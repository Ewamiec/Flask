'''COURSE PART I
flask installation (CMD):
python -m venv env
env\Scripts\activate
pip install Flask
deactivate

------------
We create the main catalog application, just next to the catalog with virtual environment. It will gather the logic of our app, 
all functions, templates, styles etc.
It is also recommended to create the tests catalog at the same level, in future we will place there a file with unit tests.

In this catalog we will find following folders and files:
Folder static – with static files (styles, pics, icons, scripts in JavaScript)
Folder templates – with page layout in HTML, main page and subpages
File main.py – main app logic that links all components which are necessary to run an application
File scripts.py – in here we will define the functions that will serve the app and transfer the data to main.py
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

#import of basic modules that are necessary for our app:
from flask import Flask, render_template, request #render_template contains system of web templates, request is responsible for
#sending request to API
from scripts import getResponseFromApi, saveToJson, readFromJson #importing scripts
from wtforms import Form, TextField, validators, StringField, SubmitField
#wtforms - if we want to have a form, 
from scripts import getResponseFromApi, saveToJson, readFromJson

'''installation of WTForms (CMD):
env\Scripts\activate
pip install Flask-WTF
deactivate'''

#Form(formularz)
class SearchForm(Form):
    #create the fields
    technology = TextField('Technologia:', validators = [validators.required()])
    place = TextField('Lokalizacja:')

#class SearchForm inherits from module class Form. We are creating 2 fields in the form: technology and place that represent those.
#validators.required() is a method that makes a particular field obligatory. 

#in order to render the template to the main webpage, in function index() which executes that we add the variable form and a class
#SearchForm assigned to that together with a parameter which downloads data from the field (request.form \n return render_template)
#with the parameters: name of the template, variable (representing for on the front) - index.html and form = form
@app.route('/')
def index():
    form = SearchForm(request.form)
    return render_template('index.html', form = form)

#page with results will be called results, we create function search_results() as a part of the routing underneath the main page
#index()
#decorator pattern @app.route adopts two URLs: app_url/results, form handling methods: GET or POST

#results
@app.route('/results', methods = ('GET', 'POST'))
#function search_results() defines how we will  import input data and download data from jobs.json
def search_results():
    if request_method == 'POST':
        #get data from forms input
        description = request.form['technology']
        location = request.form['place']
        #pass data to function and get the result
        saveToJson(description, location)
    
    #read JSON file
    all_jobs = readFromJson()

    return render_template('results.html', jobs = all_jobs, description = description, location = location)