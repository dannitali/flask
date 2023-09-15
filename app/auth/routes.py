from flask import render_template, redirect, flash
from app.auth import auth
import app
from .forms import loginForm
from flask_login import login_user, current_user ,logout_user


@auth.route('/login',
            methods = ['GET', 'POST'] )
def login():
    form = loginForm()
    if form.validate_on_submit():
        #selecciona al cliente por username
        c = app.Cliente.query.filter_by(username=form.username.data).first()
        if c is None or c.check_password(form.password.data):
            flash('usuario no existente o clave incorrecta') 
            return redirect('/auth/login')
        else:
            login_user(c, remember=True)
            return redirect ('/productos/listar')
    return render_template('login.html',
                           form = form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('cerro sesion exitosamente')
    return redirect ('/auth/login')