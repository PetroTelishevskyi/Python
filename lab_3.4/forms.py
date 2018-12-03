from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    auditory = StringField('Auditory', validators=[Length(min=-1, max=50, message='You cannot have more than 50 characters')])
    surname = StringField('Surname', validators=[Length(min=-1, max=100, message='You cannot have more than 100 characters')])
    date = StringField('Date', validators=[Length(min=-1, max=25, message='You cannot have more than 25 characters')])
    time = StringField('Time', validators=[Length(min=-1, max=40, message='You cannot have more than 40 characters')])
