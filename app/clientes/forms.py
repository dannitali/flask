from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField, PasswordField
from wtforms.validators import InputRequired , Length , Email

       
class NewClientesForm(FlaskForm) :
    
        username = StringField("Ingrese su nombre :",
                         validators = [
                             InputRequired(message='Por favor ingrese su nombre')])
        password = PasswordField("Ingrese su password :",
                         validators = [
                             InputRequired(message='Por favor ingrese su password'), Length(min=8, max=20, message='La contraseña debe tener min. 8 caracteres y max. 20')])
    
        email = StringField("Ingrese su email :",
                         validators = [
                             InputRequired(message='Por favor ingrese su email'), Email(message='Ingrese correo electronico valido')])
        
        submit = SubmitField("Guardar")
    
    
class EditClientesFrom( NewClientesForm):
    submit = SubmitField("Actualizar")
    
""" class inputNew(FlaskForm, NewClientesForm):
    submit = SubmitField("Guardar") """
