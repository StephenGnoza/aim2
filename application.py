# import for basic webpage, database
from flask import Flask, render_template, request, redirect, url_for, jsonify,\
    make_response, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, State, Month, RaceCat, RaceItem
# import for login
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import session as login_session
import httplib2
import random
import string
# import for json
import json
import requests

app = Flask(__name__)

print('Hello World')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
