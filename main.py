#imports
from flask import Flask, render_template, request 
from wtforms import Form, TextField, validators, StringField, SubmitField 
from scripts import getResponseFromApi, saveToJson, readFromJson

app = Flask(__name__) #application variable - assigning Flask to variable app where an instance of class Flask is created

#home
class SearchForm(Form):
    #create the fields
    technology = TextField('Technologia:', validators = [validators.required()])
    place = TextField('Lokalizacja:')

#routing - decorator pattern
@app.route('/')
def index():
    form = SearchForm(request.form)
    return render_template('index.html', form = form)

#results
@app.route('/results', methods = ('GET', 'POST'))
def search_results():
    if request_method == 'POST':
        #get data from forms input
        description = request.form['technology']
        location = request.form['place']
        #pass data to function and get the request
        saveToJson(description, location)
    
    #read JSON file
    all_jobs = readFromJson()

    return render_template('results.html', jobs = all_jobs, description = description, location = location)

if __name__ == '__main__':
    app.run(debug=True)
