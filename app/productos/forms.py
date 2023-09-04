from flask_wtf import FlaskForm
from wtforms import StringField ,IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed


class NewProductForm(FlaskForm) :
    nombre = StringField("Ingrese nombre producto :",
                         validators = [InputRequired(message='nombre requerido')])
    precio = IntegerField("Ingrese precio Producto",
                          validators= [
                                    InputRequired(message='precio requerido'),
                                    NumberRange(message='precio fuera de rango', 
                                    min = 10000,
                                    max = 100000)])
    
    imagen = FileField(label = "Imagen del producto", 
                       validators= [
                           FileRequired(message = "Se requiere una imagen"),
                           FileAllowed(
                               ["jpg", "png"],
                               message = " Solo se aceptan imagenes"
                           )
                       ])
    submit = SubmitField("Guardar")
    
    