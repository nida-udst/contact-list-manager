from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Regexp

class ContactForm(FlaskForm):
    first = StringField('First Name',validators=[DataRequired(), Length(min=1, max=50),Regexp(r'^[A-Za-z\s]+$', message="First name must only contain letters and spaces.")])
    last = StringField('Last Name', validators=[DataRequired(),Length(min=1, max=50),Regexp(r'^[A-Za-z\s]+$', message="Last name must only contain letters and spaces.")])
    phone = StringField('Phone')
    email = StringField('Email', validators=[DataRequired(), Email()])
    type = SelectField('Type', 
                      choices=[('Personal', 'Personal'), 
                              ('Work', 'Work'), 
                              ('Other', 'Other')])
    submit = SubmitField('Submit') 