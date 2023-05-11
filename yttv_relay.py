#!/usr/bin/env python3

from pprint import pformat
from time import time

from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify

from threading import Thread

from google_oauth import GoogleOauth

app = Flask(__name__)

auth = GoogleOauth(token_file='.authorization')

from requests_oauthlib import OAuth2Session

import os

# OAuth endpoints given in the Google API documentation


@app.route("/")
def home():
    """Step 1: User Authorization.

    Redirect the user/resource owner to the OAuth provider (i.e. Google)
    using an URL with a few key OAuth parameters.
    """
    if auth.token:
        return """
        Token already setup, nothing to do.
        """
    else:
        # State is used to prevent CSRF, keep this for later.
        authorization_url, session['oauth_state'] = auth.initial_auth_session(redirect_uri=request.base_url + 'callback')
        print(authorization_url)
        return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.
@app.route("/callback", methods=["GET"])
def callback():
    """ Step 3: Retrieving an access token.

    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """
    auth.save_token(
        state=session['oauth_state'],
        response_url=request.url,
        redirect_uri=request.base_url
    )
    return redirect(url_for('.home'))


if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0')