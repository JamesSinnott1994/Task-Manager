import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY") # Required for some Flask functions

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    # Finds all documents from the "tasks" collection on database
    tasks = mongo.db.tasks.find()

    # "tasks" passed into the tasks.html page
    # 2nd tasks below is the tasks above
    return render_template("tasks.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)