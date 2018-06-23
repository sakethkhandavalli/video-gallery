# uncompyle6 version 2.9.10
# Python bytecode 3.5 (3350)
# Decompiled from: Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
# [GCC 5.4.0 20160609]
# Embedded file name: /home/sai_kamal/main_project_itws/video_gallery/app/user/models.py
# Compiled at: 2017-04-05 09:20:39
# Size of source mod 2**32: 1108 bytes
from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.playlist.models import Playlist

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    myplaylists = db.relationship('Playlist', backref='myuser', lazy='dynamic')
    no_playlists = db.Column(db.Integer)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.no_playlists = 3
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {'user_id': self.user_id,'name': self.name,'email': self.email}

    def __repr__(self):
        return 'User<%d><%d> %s' % (self.user_id, self.no_playlists, self.name)
# okay decompiling models.cpython-35.pyc
