from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def celsius_to_fahrenheit(celsius=""):
    fahrenhiet = convert_celsius_to_fahrenheit(float(celsius))
    return f"{fahrenhiet}"


def convert_celsius_to_fahrenheit(celsius: float):
    """Convert celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
