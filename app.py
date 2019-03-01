# import flask
from flask import Flask, render_template, redirect

import os

# Create an instance of our Flask app.
app = Flask(__name__, static_url_path='/static')

#app._static_folder = os.path.join(os.path.abspath(__file__), "templates", "static")


## Import our pymongo library, which lets us connect our Flask app to our Mongo database.
#import pymongo
#
## Create connection variable
#conn = 'mongodb://localhost:27017'
#
## Pass connection to the pymongo instance.
#client = pymongo.MongoClient(conn)
#
## Connect to a database.
#db = client.mars_db
#
### NOTE: We technically could insert the data within this app.py file, but then we 
### would end up re-adding the data every time the server is loaded, unless we 
### dropped the data and reloaded in upon every server restart.

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
