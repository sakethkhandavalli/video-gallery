# Import flask and template operators
from flask import Flask, render_template, session, jsonify

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

from functools import wraps

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
   return render_template('index.html'), 404

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify(message="Unauthorized", success=False), 401
        return f(*args, **kwargs)
    return decorated

# Import a module / component using its blueprint handler variable (mod_auth)
from app.user.controllers import mod_user
from app.playlist.controllers import mod_playlist
from app.url.controllers import mod_url

from app.user.models import User
from app.playlist.models import Playlist
from app.url.models import Url

# Register blueprint(s)
app.register_blueprint(mod_user)
app.register_blueprint(mod_playlist)
app.register_blueprint(mod_url)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
