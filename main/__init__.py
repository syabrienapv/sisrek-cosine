from flask import Flask

app = Flask(__name__)

app.secret_key = "996024"

from main import routes