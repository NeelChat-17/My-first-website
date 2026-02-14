import numpy as np
import pandas as pd
from flask import Flask

@app.route('/')
def home():
  print('This is the first page that appears')

@app.route('/sign up')
def signup():
  print('This is the signup page for new user')

@app.route('/login')
def login():
    print('This is the login page already registered user')

