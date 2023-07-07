from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#SQLAlchemy é um ORM para gerir o processo de interação com o banco

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug = True)