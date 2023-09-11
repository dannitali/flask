#importaciones de dependencias

from flask import Flask, render_template
from .config import Config  #aqui el .config estamos trallendo ese modulo de Config 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .mi_blueprint import mi_blueprint
from app.productos import productos
from app.clientes import clientes
from flask_bootstrap import Bootstrap



#inicializamos el objeto flask

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)



#inicializamos el objeto SQLALchemy
db = SQLAlchemy(app)
Migrate = Migrate(app , db )



#registar modulos(blueprints)
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)
app.register_blueprint(clientes)




from .models import Cliente, Venta, Producto, Detalle # ESTO SE IMPORTA AL FINAL Y NO ARRIBA YA QUE COMO EL CODIGO SE EJECUTA LINEA POR LINEA , A LA HORA DE LLEGAR A MODELS , EN ESTE ARCHIVO SE NECESITA DB Y AQUI EN INIT , DB SE INCIALIZA MAS ABAJO 

@app.route('/prueba')
def prueba():
    return render_template("base.html")