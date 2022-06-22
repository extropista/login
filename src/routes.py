#from src import app
from src.__init__ import app
from src.config import db
from src.models.ModelUser import ModelUser  # Modelos
from src.models.entities.User import User   #Entidades
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
from flask import render_template, request, redirect, url_for, flash
import MySQLdb.cursors
import re




@app.route('/')
def index():
    return redirect(url_for('login'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('homepage'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

# Almacenamiento datos del Usuario

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


# Ruta de registro del mandato de usuario

@app.route('/mandato')
def mandato():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'direccion' in request.form and 'region' in request.form and 'comuna' in request.form and 'postalcode' in request.form and 'fullname' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        fullname = request.form['fullname']  
        direccion = request.form['direccion']
        region = request.form['region']
        comuna = request.form['comuna'] 
        postalcode = request.form['postalcode'] 
        cursor = MySQL.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'La cuenta ya existe !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Correo no válido !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'El nombre de usuario solo puede contener letras y numeros !'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s, % s, % s, % s, % s, % s)', (username, password, email, fullname, direccion, region, comuna, postalcode, ))
            MySQL.connection.commit()
            msg = 'Te has registrado correctamente !'
    elif request.method == 'POST':
        msg = 'Por favor rellene el formulario !'
    return render_template('mandato.html', title='Mandato', msg = msg)
    #return redirect(url_for('home'))




@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/homepage')
def homepage():
    return render_template('homepage.html',title='Home')

@app.route('/update')
def update():
    return render_template('update.html')


# decorated funtion...route method
@app.route('/about')
def about():
    return render_template('about.html',title='About')

# decorated funtion...route method
@app.route('/account')
def account():
    return render_template('account.html',title='Account')


    
@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"
