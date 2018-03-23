import os
from app import app, db
from .forms import UserProfileForm
from flask import render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
from .models import Users

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/profile', methods=['POST', 'GET'])
@app.route('/profile/<userid>')
def profile(userid = None):
    form = UserProfileForm()
    error = None
    if(userid):
        try: 
            user = Users.query.filter_by(userid = int(userid)).first()
            return render_template("user.html", user = user)
        except ValueError:
            pass
        abort(404)
        return "User Profile"
    elif request.method == "POST":
        if form.validate_on_submit():
            if(Users.query.filter_by(email = form.email.data).first()):
                error = "Email already in use."
            else:
                photo       = form.photo.data
                filename    = secure_filename(form.email.data.split("@")[0]+"."+photo.filename.split(".")[-1])
                db.session.add(Users(first_name = form.first_name.data, last_name = form.last_name.data, 
                                    email = form.email.data, gender = form.gender.data, photo = filename, 
                                    location = form.location.data, bio = form.biography.data))
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                db.session.commit()
                return redirect(url_for("profiles"))
        else:
            error = "Invalid Data Received"
        pass
    return render_template("profile.html", form = form, error = error)

@app.route('/profiles')
def profiles():
    users = Users.query.all()
    return render_template("profiles.html", users = users)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404