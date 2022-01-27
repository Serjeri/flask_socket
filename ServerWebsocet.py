from flask import Flask, redirect, render_template,url_for
from flask_socketio import SocketIO, emit
import random
from authlib.integrations.flask_client import OAuth



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
oauth = OAuth(app)

github = oauth.register (
  name = 'github',
    client_id = "d275dbdf14445daa91d6",
    client_secret = "95256032aeb42969d07c72dcd98c860ed347d075",
    access_token_url = 'https://github.com/login/oauth/access_token',
    access_token_params = None,
    authorize_url = 'https://github.com/login/oauth/authorize',
    authorize_params = None,
    api_base_url = 'https://api.github.com/',
    client_kwargs = {'scope': 'user:email'},
)


@socketio.on('message')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    while True:
        try:
            emit('message', {'goodbye': random.random()})                        
            socketio.sleep(5)
        except:
            pass
    

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/login')
def github_login():
    github = oauth.create_client('github')
    redirect_uri = url_for('github_authorize', _external=True)
    return github.authorize_redirect(redirect_uri)


@app.route('/login/github/authorize')
def github_authorize():
    github = oauth.create_client('github')
    token = github.authorize_access_token()
    resp = github.get('userinfo').json()
    return redirect('/')

@app.route('/logout')
def logout():
    return redirect('/login')


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
