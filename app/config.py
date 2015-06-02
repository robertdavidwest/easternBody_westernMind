# config.py
import os

# grab the foler where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'easternBody_westernMind.db'
CSRF_ENABLED = True
SECRET_KEY = 'TEST123'

# the full database path
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
