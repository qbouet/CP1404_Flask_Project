"""
CP1404 Prac 10 Flask Project
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Normal function that prints hello world"""
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """Greet person using their name"""
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius=""):
    """Convert fahrenheit to celsius"""
    return str(convert_celsius_to_fahrenheit(float(celsius)))


def convert_celsius_to_fahrenheit(celsius):
    """Convert fahrenheit to celsius"""
    return celsius * 9.0 / 5 + 32


if __name__ == '__main__':
    app.run()
