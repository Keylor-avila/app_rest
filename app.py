from flask import Flask, render_template, request, redirect,  url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'keylor'
app.config['MYSQL_PASSWORD'] = '*KylR2407*'
app.config['MYSQL_DB'] = 'rest_app'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/', methods = ['POST'])
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM rest_app')
    data = cur.fetchall()
    return render_template('loginPJ.html', rest_app=data)

@app.route('/perfil')
def Perfil():
    return render_template('pdusuarioPJ.html')

@app.route('/login', methods = ['POST'])
def Login():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM rest_app')
    data = cur.fetchall()
    return render_template('loginPJ.html', rest_app =data)

@app.route('/new_log')
def new_log():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('''INSERT INTO login (username, email, password) 
                                    VALUES (%s, %s, %s)''',
                    (username, email, password))
        mysql.connection.commit()
        flash('Registro exitoso')
        return redirect(url_for('Perfil'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)