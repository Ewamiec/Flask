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

-->models.py {import requests, import json}

Step III - defininig a funcions that uploads data with 2 parameters - description and location'''
def getResponseFromApi(description, location):