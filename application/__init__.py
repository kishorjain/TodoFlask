from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"]="0093ed739d5cfa630425233a1c354e1fbcebdeb5"
app.config["MONGO_URI"]="mongodb://localhost:27017/myDatabase"

mongodb_client = PyMongo(app)
db = mongodb_client.db
from application import routes