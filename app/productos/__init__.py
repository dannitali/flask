from flask import Blueprint
productos = Blueprint('productos',
                      __name__,
                      url_prefix = '/productos',
                      template_folder ='templates',
                      static_folder='imagenes')


from . import routes #ese . import es para importar todo loq ue halla en routes
