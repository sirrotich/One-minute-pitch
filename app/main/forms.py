from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch Title',validators=[Required()])
    category = SelectField(u'Pitch Category', choices = [('', 'life'), ('coding', 'coding'), ('funny', 'funny')])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = TextAreaField('Comment')
    submit = SubmitField('Submit') 

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you', validators=[Required()])
    submit = SubmitField('Submit')