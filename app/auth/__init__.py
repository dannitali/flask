from flask import Blueprint
auth = Blueprint('auth',
                      __name__,
                      url_prefix = '/auth',
                      template_folder ='templates')


from . import routes #ese . import es para importar todo loq ue halla en routes
