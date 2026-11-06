from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from database import *

app = Flask(__name__)
app.secret_key = 'lana=linda-perfeita-maravilhosa'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Faça login para acessar'
login_manager.init_app(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@login_manager.user_loader
def load_user(user_id):
    return db_session.get(User, int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', register_user=request.args.get('register_user') == True)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('login.html')
@app.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)