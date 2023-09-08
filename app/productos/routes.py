from flask import render_template, redirect, flash 
from app.productos import productos
import app
import os 
from .forms import NewProductForm, EditProducFrom


@productos.route('/create', methods = ['GET', 'POST'])

def crear():
    p = app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        #subir imagen a carpeta / imagenes
        archivo=form.imagen.data
        archivo.save(os.path.abspath(os.getcwd() + "/app/productos/imagenes/" + p.imagen))
        flash("producto registrado exitosamente")
        return redirect ('/productos/listar')
    return render_template('new.html',
                           form = form)


@productos.route('/listar')
def listar():
    #selecionar los productos
    productos = app.models.Producto.query.all()
    return render_template ("list.html", 
                            productos = productos)

    
@productos.route('/editar/<producto_id>',
                 methods = ['GET', 'POST'])
def editar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    form = EditProducFrom(obj=p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('producto actualizado')
        return redirect('/productos/listar')
    return render_template('new.html', 
                           form=form)


@productos.route('/eliminar/<producto_id>')
def eliminar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    app.db.session.delete(p)
    app.db.session.commit()
    flash('producto eliminado')
    return redirect('/productos/listar')
