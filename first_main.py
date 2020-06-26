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