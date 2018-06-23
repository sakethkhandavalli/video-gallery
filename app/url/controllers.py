from datetime import datetime
from flask import Blueprint, request, session, jsonify
from app import db, requires_auth
from .models import *
from app.user.models import *
from app.playlist.models import *
from sqlalchemy import *
import datetime

mod_url = Blueprint('url', __name__, url_prefix='/api')


@mod_url.route('/addurl/global', methods=['POST'])
@requires_auth
def add_url_global():
    url = request.form['url']
    name = request.form['name']
    user_id = session['user_id']
    #favorite = request.form['favorite']
    #watch_later = request.form['watch_later']
 #   user=User.query.filter(User.user_id == user_id).first()
    recent = Playlist.query.filter(and_(Playlist.title == 'recent', Playlist.user_id == user_id)).first()
    print(user)
#    playlist = Playlist.query.filter(and_(Playlist.myuser == user, Playlist.title == name)).first()
#   print(playlist)
   # if not Url.query.filter(Url.url == url):
    urls = Url.query.filter(and_(Url.url == url , Url.playlist_id == recent.playlist_id)).first()
    if urls:
        return jsonify(success=False,message='this url already exists in this recent playlist')
    else:
        obj = Url(url, name, recent.playlist_id, user_id)
    print(obj)
    db.session.add(obj)
    try:
        db.session.commit()
    except:
        print('Commit Error')
    return jsonify(success=True)

@mod_url.route('/addurl/local', methods=['POST'])
@requires_auth
def add_url_local():
    url = request.form['url']
    name = request.form['name']
    playlist_id = request.form['playlist_id']
    user_id = session['user_id']
    print('url',url)
    print('name',name)
    print('playlist_id',playlist_id)
    print('user_id',user_id)
    recent = Playlist.query.filter(and_(Playlist.title == 'recent', Playlist.user_id == user_id)).first()
    urls = Url.query.filter(and_(Url.url == url , Url.playlist_id == playlist_id)).first()
    if urls:
        return jsonify(success=False,message='this url already exists in this playlist')
    else:
        obj = Url(url, name, playlist_id, user_id)
        db.session.add(obj)
        db.session.commit()
        if not Url.query.filter(and_(Url.url == url , Url.playlist_id == recent.playlist_id)).first():
            obj_recent = Url(url, name, recent.playlist_id, user_id)
            db.session.add(obj_recent)
    print(obj)
    try:
        db.session.commit()
    except:
        print('Commit Error')
        return jsonify(success=False)
    return jsonify(success=True)

@mod_url.route('/url/delete/global', methods=['POST'])
@requires_auth
def delete_url_global():
    url_id = request.form['url_id']
    user_id = session['user_id']
    url = Url.query.filter(and_(Url.url_id == url_id, Url.user_id == user_id)).first()
    if url is None:
        return jsonify(success=False, message='this url doesnt exist'), 404
    else:
        urls = Url.query.filter(and_(Url.url == url.url, Url.user_id == user_id)).all()
        for i in urls:
            db.session.delete(i)
    db.session.commit()
    return jsonify(success=True)

@mod_url.route('/url/delete/local', methods=['POST'])
@requires_auth
def delete_url_local():
    url_id = request.form['url_id']
    playlist_id = request.form['playlist_id']
    url = Url.query.filter(and_(Url.name == url_id, Url.playlist_id == playlist_id)).first()
    if url is None:
        return jsonify(success=False,message='this url doesnt exist in this playlist'), 404
    else:
        db.session.delete(url)
    db.session.commit()
    return jsonify(success=True)

@mod_url.route('/url/edit/global', methods=['POST'])
@requires_auth
def edit_url_global():
    url_id = request.form['url_id']
    user_id  = session['user_id']
    url_name=request.form['url_name']
    urls = Url.query.filter(and_(Url.url_id == url_id, Url.user_id == user_id)).all()
    if urls is None:
        return jsonify(success=False, message='this url doesnt exist'), 404
    else:
        for i in urls:
            i.name=url_name
    db.session.commit()
    return jsonify(success=True)

@mod_url.route('/url/modify', methods=['POST'])
@requires_auth
def modify_url_global():
    url = request.form['url_id']
    user_id  = session['user_id']
    recent = Playlist.query.filter(and_(Playlist.title == 'recent',Playlist.user_id == user_id)).first()
    url = Url.query.filter(and_(Url.playlist_id == recent.playlist_id, Url.url == url)).first()
    if url is None:
        return jsonify(success=False, message='this url doesnt exist'), 404
    else:
        url.time = datetime.datetime.utcnow()
    db.session.commit()
    print('modified')
    return jsonify(success=True),200
