from flask import Flask
from flask import jsonify

from scraper import scrape

app = Flask(__name__)


@app.route('/api/v1/garages')
@app.route('/api/v1/garages/')
def garages():
    return jsonify(scrape())


@app.route('/api/v1/garages/<garage>')
@app.route('/api/v1/garages/<garage>/')
def garage(garage):
    garage = filter(lambda x: x['name'].lower() == garage.lower(), scrape())
    return jsonify(garage)


if __name__ == '__main__':
    app.run()
