# config                    
from flask import Flask
app = Flask(__name__)

#index route
@app.route('/')
def index():
    return 'Hello, this is PetFax!'

@app.route('/pets')
def pets():
    return 'These are out pets avalible for adoption!'