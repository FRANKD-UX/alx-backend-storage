#!/usr/bin/env python3
"""
A Flask app with a mock user login system.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Dict, Union

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Configuration class for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Union[Dict, None]:
    """
    Retrieves a user dictionary based on the 'login_as' URL parameter.

    Returns:
        A user dictionary or None if the user ID is not found.
    """
    user_id = request.args.get('login_as')
    if user_id:
        try:
            return users.get(int(user_id))
        except (ValueError, TypeError):
            return None
    return None


@app.before_request
def before_request() -> None:
    """
    Sets the user in the global context `g` before each request.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best language match.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the index page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
