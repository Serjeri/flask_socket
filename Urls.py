from flask import redirect, render_template,url_for
from authlib.integrations.flask_client import OAuth
from ServerWebsocet import app

class Urls:
    oauth = OAuth(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login')
    def github_login(self):
        github = self.oauth.create_client('github')
        redirect_uri = url_for('github_authorize', _external=True)
        return github.authorize_redirect(redirect_uri)

    @app.route('/login/github/authorize')
    def github_authorize(self):
        github = self.oauth.create_client('github')
        token = github.authorize_access_token()
        resp = github.get('userinfo').json()
        return redirect('/')

    @app.route('/logout')
    def logout(self):
        return redirect('/login')