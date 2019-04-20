from flask import render_template
from app import app
from .forms import RegistrationForm

#views
@main.route('/')
def index():
    title = 'Home - Great chnage start with you'
    return render_template('index.html', title = title)

@main.route('/new_pitch/<int:id>')
def new_pitch():
     return render_template('new_pitch.html')
