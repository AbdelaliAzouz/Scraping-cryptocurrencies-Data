from logging import exception
from  flask import Flask, redirect, request
from flask.templating import render_template
from requests import request
import requests 
from scrape import *
from bson.json_util import dumps
import json

from pymongo import MongoClient



client = MongoClient('localhost:27017')
db = client.ContactDB

app = Flask(__name__)


@app.route('/')    
def home():
    scrape_mongo()
    return render_template('index.html')
#======================data scraping endpoint=======================

@app.route('/scrape_data', methods = ['POST'])
def scrape():
    try:
       pass
    except Exception as e:
        return dumps({'error' : str(e)})

#=====================data visualization endpoint ======================================
@app.route('/visualize', methods=['GET'])
def visualize():
    #Get data from mongo for visualization purpose
    try:
        currencies = scrape.crypto.find()
        return dumps(currencies)
    except Exception as e:
        return dumps({'error' : str(e)})


if __name__ == '__main__':
    app.run(debug = True)

