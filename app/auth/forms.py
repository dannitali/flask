from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField, SubmitField
from wtforms.validators import InputRequired, NumberRange , Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class loginForm(FlaskForm):
    username=StringField(label="nombre de usuario:",
                         validators = [
                             InputRequired(message='nombre requerido')])
    password=PasswordField(label="clave")
    submit=SubmitField(label="iniciar sesion")




