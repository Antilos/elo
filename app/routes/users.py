from flask import Blueprint, request, render_template, flash, redirect, url_for

from app.forms import RegisterForm
from app.models import User
from app import db

bp = Blueprint('users', __name__, url_prefix="/user")

@bp.route('/__all')
def allUsers():
    users = User.query.all()
    return render_template('users/allUsers.html', title="All Users", users = users)

@bp.route('/<username>/profile')
def userProfile(username):
    #get the user if it exists
    user = User.query.filter_by(username=username).first_or_404()
    
    return render_template('users/userProfile.html', title="User Profile", user = user)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, elo=1000)
        db.session.add(user)
        db.session.commit()

        flash(f'Registered user {user.username}.')
        return redirect(url_for('index'))
    return render_template('auth/register.html', title='Register', form=form)
