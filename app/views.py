"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from flask import render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from app import app
from flask_wtf import FlaskForm
from app.models import UserProfile, db
import random
import os
import time

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')         


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/Profile_data', methods=['POST', 'GET'])
def signup():
    """Render website's home page."""
    
    if request.method == 'POST':
        db.create_all()
        #userid = str(uuid.uuid4().fields[-1])[:8]
        userid = str(random.randint(0,99999999))
        tim = time.strftime("%a, %d %b %Y")
        pic = request.files['profilepic']
        #fil = file.filename
        if pic:
            file_folder = app.config['UPLOAD_FOLDER']
            filename = secure_filename(pic.filename)
            pic.save(os.path.join(file_folder, filename))
        profiles = UserProfile(userid, request.form['username'],tim , request.form['fname'],request.form['lname'], filename, request.form['age'], request.form['gender'], request.form['bio'])
       # profiles.set_id(userid)
        db.session.add(profiles)
        db.session.commit()
        flash('New person was added ')
        return redirect(url_for('profiles'))
    return render_template('Profile_data.html')

###
# The functions below should be applicable to all Flask apps.
###
@app.route('/profiles', methods=['GET','POST'])
def profiles():
    # rootdir = os.getcwd()
    profslist = []
    profs = UserProfile.query.filter_by().all()
    if request.method == 'POST':
        for prof in profs:
            profslist += [{'username': prof.username, 'userid': prof.id}]
        return jsonify(profs=profslist)
    elif request.method == 'GET':
        return render_template('profiles.html', profs=profs)
    return redirect(url_for('home'))

@app.route('/profile/<id>', methods=['GET','POST'])
def profile(id):
    profsjson = {}
    user = UserProfile.query.filter_by(id=id).first_or_404()
    if request.method == 'POST':
        profsjson = {'userid':user.id, 'username':user.username, 'image':user.image, 'gender':user.gender, 'age':user.age, 'profile_created_on':user.profile_created_on}
        return jsonify(profsjson)
    elif request.method == 'GET' and user:
        return render_template('show_users.html',profile=user)
    return render_template('profile_data.html')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)
    
# @login_manager.user_loader
# def load_user(id):
#     return UserProfile.query.get(int(id))

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")