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

@main.route('/pitch/', methods = ['GET', 'POST'])
@login_required
def new_pitch():

     form = PitchForm()

     if form.validate_on_submit():
          category = form.category.data
          pitch = form.pitch.data
          comment = form.comment.data

          new_pitch = Pitches(title = title, category = category, pitch = pitch, user_id=current_user_id)

          title = 'New Pitch'

          new_pitch.save_pitch()

          return redirect(url_for('main.index'))
     return render_template('pitch.html', pitch_entry = form)

@main.route('/user/<uname>')
def category(cate):
     '''
     returns pitches byt category
     '''
      category = Pitches.get_pitches(cate)
      title = f'{cate}'
      return render_template('categories.html',title = title, category = category)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.author))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(author = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/comments/<id>')
@login_required
def comment(id):
    '''
    function to return the comments
    '''
    comm =Comments.get_comment(id)
    print(comm)
    title = 'comments'
    return render_template('comments.html',comment = comm,title = title)






