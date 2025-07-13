#!/usr/bin/env python3
"""
A basic Flask app with Babel for i18n.
"""
from flask import Flask, render_template
from flask_babel import Babel


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


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the index page.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
