from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Clientes(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    telefone = db.Column(db.String(10))

    def __init__(self, username, name, email, telefone, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.telefone = telefone
        
db.create_all()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template("cadastro.html")

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        username = request.form.get('username')
        telefone = request.form.get('telefone')
        senha = request.form.get('senha')
        email = request.form.get('email')


if __name__ == '__main__':
    app.run(debug=True)