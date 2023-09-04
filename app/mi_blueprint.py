from flask import Blueprint

mi_blueprint = Blueprint('blueprint',  #'blueprint' es el nombre del modulo
                         __name__,
                         url_prefix = "/modulo")

@mi_blueprint.route('/ejemplo')
def ejemplo ():
    return 'estoy en blueprint'