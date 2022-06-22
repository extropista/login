from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo, Email


class RegistrationForm(FlaskForm):
    username= StringField(label='Username',validators=[DataRequired(),Length(min=3,max=20)])
    email= StringField(label='Email',validators=[DataRequired(),Email()])
    password= PasswordField(label='Clave',validators=[DataRequired(),Length(min=7,max=20)])
    confirm_password= PasswordField(label='Confirmar Clave',validators=[DataRequired(),EqualTo(password)])
    submit= SubmitField('Inscribirse')

class LoginForm(FlaskForm):
    username= StringField(label='Username',validators=[DataRequired(),Length(min=3,max=20)])
    password= PasswordField(label='Clave',validators=[DataRequired(),Length(min=7,max=20)])
    submit= SubmitField('Ingresar')    