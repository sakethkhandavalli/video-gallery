from flask import Blueprint, request, session, jsonify
from app import db, requires_auth
from .models import *
from app.user.models import *
from operator import attrgetter
from app.url.models import *
from app.url.controllers import *
from sqlalchemy import and_
mod_playlist = Blueprint('playlist', __name__, url_prefix='/api')


@mod_playlist.route('/playlist/create', methods=['POST'])
@requires_auth  #it is a decorator, decorates the function ,it is also a wrapper.
def create_playlist():
    title = request.form['title']
    user_id = session['user_id']
    playlist = Playlist(title, user_id)
    user = User.query.filter(User.user_id == user_id).first()
    user.no_playlists = user.no_playlists+1
    #myuser = Playlist.query.filter(Playlist.user_id == user_id).first()
    #myuser.no_playlists = myuser.no_playlists + 1
    db.session.add(playlist)
    try:
    	db.session.commit()
    except IntegrityError:
    	return jsonify(success=False,message="check the details"), 400
    return jsonify(success=True, playlist=playlist.to_dict())


# Return a json object that has the titles recent , favorites , watch_later and
# each of the titles has all the url's to be stored for that corresponding playlist 

@mod_playlist.route('/playlist/getap', methods=['GET'])
@requires_auth
def get_all_playlists():
    user_id = session['user_id']
    arr_ids=[]
    arr_titles=[]
    arr_urls=[]
    saketh=[]
    saketh_ids = []
    playlist = Playlist.query.filter(and_(Playlist.user_id == user_id, Playlist.title == 'recent')).first()
    urls = Url.query.filter(and_(Url.user_id == user_id,Url.playlist_id == playlist.playlist_id)).all()
    urls.sort(key = lambda x:x.time,reverse=True)
    print(urls)
    for i in urls:
        saketh.append(i)
        saketh_ids.append(i.url_id)
    user = User.query.filter(User.user_id ==user_id).first()
    playlists = Playlist.query.filter(Playlist.user_id == user_id).all()
    global temp
    global temper
    temp=[[] for i in range(user.no_playlists)]
    temper=[[] for i in range(user.no_playlists)]
    count = 0
    for i in playlists:
        arr_ids.append(i.playlist_id)
        arr_titles.append(i.title)
        urls = Url.query.filter(Url.playlist_id == i.playlist_id).all()
        urls.sort(key = lambda x:x.time,reverse=True)
        for j in urls:
            temp[count].append(j.name)
            temper[count].append(j.url)
        count = count + 1
    return render_template('dashboard.html', arr_ids = arr_ids, arr_titles =
            arr_titles, arr_urls = temp,saketh = saketh, arr_urls_length =
            len(saketh), url_ids = saketh_ids , urls = temper, no_playlists = user.no_playlists)


@mod_playlist.route('/playlist/single', methods=['GET'])
@requires_auth
def get_playlist():
    playlist_id = request.form['playlist_id']
    user_id = session['user_id']
    global arr_urls_local
    arr_urls_local=[]
    temper=[]
    tempest=[]
    playlist = Playlist.query.filter(and_(Playlist.playlist_id == playlist_id, Playlist.user_id == user_id)).first()
    if playlist is None:
        return jsonify(success=False), 404
    else:
        urls = Url.query.filter(Url.playlist_id == playlist_id).all()
        for i in urls:
            arr_urls_local.append(i.url)
            temper.append(i.url_id)
            tempest.append(i.name)
            print(len(arr_urls_local))
       # return jsonify(success=True, playlist=playlist.to_dict(), arr_urls = arr_urls)
    return render_template('playlist.html', playlist_id = playlist_id,
            playlist_title = playlist.title, arr_urls =
            arr_urls_local,arr_urls_length=len(arr_urls_local) , url_ids=temper,url_titles=tempest)


@mod_playlist.route('/playlist/edit', methods=['POST'])
@requires_auth
def edit_playlist():
    playlist_id = request.form['playlist_id']
    user_id = session['user_id']
    playlist = Playlist.query.filter(and_(Playlist.playlist_id == playlist_id, Playlist.user_id == user_id)).first()
    if playlist is None:
        return jsonify(success=False), 404
    else:
        playlist.title = request.form['title']
    try:
    	db.session.commit()
    except IntegrityError:
    	return jsonify(success=False,message="check the details(a playlist exists with this name already)"), 400
    return jsonify(success=True)


@mod_playlist.route('/playlist/delete', methods=['POST'])
@requires_auth
def delete_playlist():
    playlist_id = request.form['playlist_id']
    user_id = session['user_id']
    playlist = Playlist.query.filter(and_(Playlist.playlist_id == playlist_id, Playlist.user_id == user_id)).first()
   # myuser = Playlist.query.filter(Playlist.user_id == user_id).first()
    #myuser.no_playlists = myuser.no_playlists - 1
    if playlist is None:
        return jsonify(success=False), 404
    else:
        urls = Url.query.filter(Url.playlist_id == playlist_id).all()
        for i in urls:
            db.session.delete(i);
        db.session.delete(playlist)
    db.session.commit()
    return jsonify(success=True)

@mod_playlist.route('/get', methods=['GET'])
@requires_auth
def getAll():
    user_id = session['user_id']
    arr_ids=[]
    arr_titles=[]
    arr_urls=[]
    user = User.query.filter(User.user_id ==user_id).first()
    playlists = Playlist.query.filter(Playlist.user_id == user_id).all()
    global temp
    global temper
    temp=[[] for i in range(user.no_playlists)]
    temper=[[] for i in range(user.no_playlists)]
    print ('temp:',temp)
    count = 0
    print ('playlists:',playlists)
    for i in playlists:
        arr_ids.append(i.playlist_id)
        arr_titles.append(i.title)
        urls = Url.query.filter(Url.playlist_id == i.playlist_id).all()
        urls.sort(key = lambda x:x.time,reverse=True)
        for j in urls:
            temp[count].append(j.name)
            temper[count].append(j.url)
        count = count + 1
    dict = {'urls': temper,'names': temp,'id': arr_ids}    
    return jsonify(dict)
