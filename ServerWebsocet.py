from flask import Flask, redirect, render_template,url_for, session
from flask_socketio import SocketIO, emit
import random
from authlib.integrations.flask_client import OAuth


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
oauth = OAuth(app)

github = oauth.register (
  name = 'github',
    client_id = "client_id",
    client_secret = "client_secret",
    access_token_url = 'https://github.com/login/oauth/access_token',
    access_token_params = None,
    authorize_url = 'https://github.com/login/oauth/authorize',
    authorize_params = None,
    api_base_url = 'https://api.github.com/',
    client_kwargs = {'scope': 'user:email'},
)

# Сервер генерирует число и отправляет на клиент
@socketio.on('message')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))# Подтверждение на подключение клиента
    while True:
        try:
            emit('message', {'goodbye': random.random()})# Отправка рандомного числа на клиент
            socketio.sleep(5)# Задержка в 5 сек на отправку
        except:
            pass
    

@app.route('/')
def index():# Не реализована не хватило времени разобраться
            # Ограничение прав доступа
    return render_template('index.html')

@app.route('/login')
def github_login():# Авторизация на github
    github = oauth.create_client('github')
    redirect_uri = url_for('github_authorize', _external=True)
    return github.authorize_redirect(redirect_uri)

@app.route('/login/github/authorize')
def github_authorize():
    github = oauth.create_client('github')
    tokenId = github.authorize_access_token()
    session['api_session_token'] = tokenId['access_token']
    return redirect('/')

@app.route('/logout')
def logout():
    return redirect('/login')


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
