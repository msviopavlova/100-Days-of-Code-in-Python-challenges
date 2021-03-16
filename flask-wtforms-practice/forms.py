from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Login_form(FlaskForm):
    email = StringField('email')
    password = StringField('password')