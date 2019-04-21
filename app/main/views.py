from flask import render_template,redrect,url_for
from . import main
from .. import db,photos
from ..models import Pitches,Users,Comments
from .forms import PitchForm,CommentForm,UpdateProfile
from flask_login import login_required,current_user



#views
@main.route('/')
def index():
    title = 'Home - Great chnage start with you'
    return render_template('index.html', title = title)

@main.route('/new_pitch/<int:id>')
@login_required
def new_pitch():
     return render_template('new_pitch.html')

