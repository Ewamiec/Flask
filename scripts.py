'''COURSE PART II
Purpose of this app is to gownload data (job offers) from GitHubJobs API, store it in JSON file and then display it on front.
In the file of scripts.py we will define the functions that send a request to API, receive data and save it in JSON.
Basic query for data download to API is following:
https://jobs.github.com/positions.json?description=python&location=new+york
our query begins after ? --> description=python&location=new+york
description --> used technology
location --> location LUL

Next step - open CMD and install Python modules that will serve our function: module requests and json:

cmd:
env\Scripts\activate
pip install requests
deactivate

-->models.py {import requests, import json}'''
import requests
import json

'''Step III - defininig a funcions that uploads data with 2 parameters - description and location'''
def getResponseFromApi(description, location):

    global response_result

    basic_url = 'https://jobs.github.com/positions.json'
    params_to_pass = {
        'description': description,
        'location': location
    }

    response_result  = request.get(basic_url, params = params_to_pass)
    return response_result

'''requests.get sends a query to the server and awaits its answer. If the response status == 200, it would mean that the server
enables such connection and an access for data upload.
Next: two additional functions of saveToJson() and readFromJson() that will conduct data saving to JSON and reading them.'''

#Save response data to JSON file
def saveToJson(description, location):
    getResponseFromApi(description, location)
    with open('jobs.json', 'w', encoding = 'utf-8') as file:
        file.write(response_result.text)

#Read data from JSON file: a function that opens JSON file thanks to which we read the data and will pass it to the front (similar
# to the previous funcion but without adding a flag)
def readFromJson():
    with open('jobs.json', encoding='utf-8') as jobs_file:
        load_jobs = json.load(jobs_file)
        return load_jobs


