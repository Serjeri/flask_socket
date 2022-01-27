from Urls import oauth
from Urls import Urls
from Urls import OAuth
from ServerWebsocet import app

class Settings(Urls):
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