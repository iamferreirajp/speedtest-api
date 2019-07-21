import os
import json
import functools
import google.oauth2.credentials
import googleapiclient.discovery
from flask import Flask
from service import google_auth
from authlib.client import OAuth2Session

app = Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)
app.register_blueprint(google_auth.app)

@app.route('/')
def index():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"

    return 'You are not currently logged in.'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')