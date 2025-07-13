#!/usr/bin/env python3
"""
A Flask app that infers the appropriate timezone.
"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union

# ... (Copy users dictionary, Config, app, babel, get_user, before_request from 6-app.py) ...
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

def get_user() -> Union[Dict, None]:
    user_id = request.args.get('login_as')
    if user_id:
        try:
            return users.get(int(user_id))
        except (ValueError, TypeError):
            return None
    return None

@app.before_request
def before_request() -> None:
    g.user = get_user()

@babel.localeselector
def get_locale() -> str:
    # ... (Copy get_locale from 6-app.py) ...
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone() -> str:
    """
    Determines the best timezone match based on a priority order.
    1. Timezone from URL parameters
    2. Timezone from user settings
    3. Default to UTC
    """
    # 1. Find timezone parameter in URL parameters
    tz = request.args.get('timezone')
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # 2. Find time zone from user settings
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # 3. Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the index page.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
