
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)

mongo = PyMongo(app)

conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = mongo.db.mars


@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template("mars.html", mars=mars)

@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    mars_data = mars_scrape.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run(debug=True)