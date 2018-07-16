from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql

app = Flask(__name__)
app.config.from_object(Config)
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
