from flask import Blueprint
clientes = Blueprint('clientes',
                      __name__,
                      url_prefix = '/clientes',
                      template_folder ='templates')


from . import routes #ese . import es para importar todo loq ue halla en routes
