import json, requests
from time import time
from requests_oauthlib import OAuth2Session

class GoogleOauth(object):
    def __init__(self, token_file=None):
        self.token_file = token_file
        self.client_id = '<your-app-id>.apps.googleusercontent.com'
        self.client_secret = '<your-app-secret>'
        self.extra = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        self.authorization_base_url = "https://accounts.google.com/o/oauth2/v2/auth"
        self.token_url = "https://www.googleapis.com/oauth2/v4/token"
        self.scope = [
            "https://www.googleapis.com/auth/youtube"
        ]
        self._token = None


    @property
    def token(self):
        if self._token is None:
            try:
                with open(self.token_file, "r") as token_file:
                    self._token = json.loads(token_file.read())
                self._token['expires_at'] = time() - 10
                return self._token
            except Exception as error:
                print('Error setting up token: %s' % error)
                return False
        else:
            return self._token

    @token.setter
    def token(self, token):
        if self.token_valid(token):
            with open(self.token_file, 'w') as auth:
                auth.write(json.dumps(token))
            self._token = token

    def set_token(self, token):
        self.token = token

    def token_valid(self, token):
        validate_url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?'
                        'access_token=%s' % token['access_token'])
        if 'error' in requests.get(validate_url).json():
            return False
        else:
            return True

    def initial_auth_session(self, redirect_uri):
        google = OAuth2Session(self.client_id, scope=self.scope, redirect_uri=redirect_uri)
        return google.authorization_url(self.authorization_base_url,
            # offline for refresh token
            # force to always make user click authorize
            access_type="offline", prompt="consent")

    def save_token(self, state, response_url, redirect_uri):
        google = OAuth2Session(self.client_id, redirect_uri=redirect_uri,
                               state=state)
        token = google.fetch_token(self.token_url, client_secret=self.client_secret,
                                authorization_response=response_url)
        self.token = token

        return True

    def get_request_session(self):
        oauth_token = self.token
        if oauth_token:
            return OAuth2Session(self.client_id,
                                 token=oauth_token,
                                 auto_refresh_kwargs=self.extra,
                                 auto_refresh_url=self.token_url,
                                 token_updater=self.set_token)
        else:
            return False
