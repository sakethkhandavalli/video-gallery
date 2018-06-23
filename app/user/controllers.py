from flask import Blueprint, request, session, jsonify, make_response, \
    render_template, redirect, url_for
from sqlalchemy.exc import IntegrityError
from app import db
from .models import *
from app.playlist.models import *
from app.playlist.controllers import *
import re

mod_user = Blueprint('user', __name__, url_prefix='/api')


def count_word(word):
    count = 0
    for i in word:
        if i:
            count = count + 1
    return count


@mod_user.route('/front', methods=['GET'])
def front():
    return render_template('front.html')


@mod_user.route('/checklogin', methods=['GET'])
def check_login():
    if 'user_id' in session:
        user = User.query.filter(User.id == session['user_id']).first()
        return jsonify(success=True, user=user.to_dict())

    return (jsonify(success=False), 401)


@mod_user.route('/login', methods=['POST'])
def login():
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError as e:
        return (jsonify(success=False,message='%s not sent in the request' % e.args), 400)

    user = User.query.filter(User.email == email).first()
    if user is None or not user.check_password(password):
        return (jsonify(success=False,message='Invalid Credentials/wrong password'), 400)

    session['user_id'] = user.user_id
    print(session['user_id'])
    return redirect(url_for('playlist.get_all_playlists'))


@mod_user.route('/logout', methods=['POST'])
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return jsonify(success=True)

'''
@mod_user.route('/showlogin', methods=['GET'])
def show_login():
    return render_template('login.html')


@mod_user.route('/showregister', methods=['GET'])
def show_register():
    return render_template('register.html')
'''

@mod_user.route('/register', methods=['POST'])
def create_user():
    try:
        name = str(request.form['name'])
        email = str(request.form['email'])
        password = str(request.form['password'])
    except KeyError as e:
        return (jsonify(success=False,
                message='%s not sent in the request' % e.args), 400)

    min_count = count_word(password)
    if min_count >= 8:
        string = re.search(r'[0-9]+', password)
        if string:
            string = re.search(r'[a-z]+', password)
            if string:
                string = re.search(r'[A-Z]+', password)
                if string:
                    string = re.search(r'^[a-zA-Z0-9_]+', password)
                    if not string:
                        return (jsonify(success=False, message='special character not included'), 400)
                else:
                    return (jsonify(success=False, message='uppercase character not included'), 400)
            else:
                return (jsonify(success=False, message='lowercase character not included'), 400)
        else:
            return (jsonify(success=False, message='number character not included'), 400)
    else:
        return (jsonify(success=False, message='password length insufficient'), 400)

    if '@' not in email:
        return (jsonify(success=False, message='Please enter a valid email'), 400)

    u = User(name, email, password)
    db.session.add(u)
    try:
        db.session.commit()
    except IntegrityError as e:
        return (jsonify(success=False, message='This email already exists'), 400)
    print('user_id:',u.user_id)
    one = Playlist('favorites', u.user_id)
    two = Playlist('watch_later', u.user_id)
    three = Playlist('recent', u.user_id)
    db.session.add(three)
    db.session.add(one)
    db.session.add(two)
    try:
        db.session.commit()
    except IntegrityError as e:
        return (jsonify(success=False, message='This email already exists'), 400)
    print(one,two,three)
    return jsonify(success=True)


@mod_user.route('/show', methods=['GET'])
def all_users():
    users = User.query.all()
    array = []
    for i in users:
        array.append(i.to_dict())
    return render_template('all.html', array=array)
