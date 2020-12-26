from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ineligible.db' # Sets ineligble.db as default database
app.config['SQLALCHEMY_BINDS'] = {'valid emails' : 'sqlite:///valid.db'} # Creates additional database for valid email addresses

db = SQLAlchemy(app)

from website import routes