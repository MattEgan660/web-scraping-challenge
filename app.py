from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)

@app.route("/")





if __name__ == "__main__":
    app.run(debug=True)
