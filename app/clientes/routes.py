from flask import render_template, redirect, flash, url_for
from app.clientes import clientes
import app
from .forms import NewClientesForm, EditClientesFrom


@clientes.route('/create', methods = ['GET', 'POST'])

def crear():
    p = app.models.Cliente()
    form = NewClientesForm()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        #subir imagen a carpeta / imagenes
        flash("clientes registrado exitosamente")
        return redirect ('/clientes/listar')
    return render_template('new_cliente.html',
                           form = form)


@clientes.route('/listar')
def listar():
    #selecionar los clientes
    clientes = app.models.Cliente.query.all()
    return render_template ("listar.html", 
                            clientes = clientes)

    
@clientes.route('/editar/<id>', methods = ['GET', 'POST'])
def editar(id):
    p = app.models.Cliente.query.get(id)
    form = EditClientesFrom(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Cliente actualizado')
        return redirect (url_for('clientes.listar'))
    return render_template('new_cliente.html', 
                           form=form)


@clientes.route('/eliminar/<id>', methods = ['GET', 'POST'])
def eliminar(id):
    id = app.models.Cliente.query.get(id)
    eliminar = id
    if eliminar:
        app.db.session.delete(eliminar)
        app.db.session.commit()
        flash(f'clientes {id} eliminado')
        return redirect(url_for('clientes.listar'))
    return render_template('listar.html')

