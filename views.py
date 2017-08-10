import logging
from flask import Flask
from flask.templating import render_template
import load_results
from load_results import parse_results, get_table, get_table_json, get_personal_json
import json
from requests.exceptions import ConnectionError


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("table.html")


@app.route('/table/')
def table():
    try:
        app.logger.info(f'Sending request to ejudge: {load_results.TABLE_URL}')
        table = get_table(load_results.TABLE_URL)
        app.logger.info('Got response from ejudge')
        parsed_table = parse_results(table)
        return get_table_json(parsed_table)
    except ConnectionError:
        app.logger.error('Ejudge not responding')
        return json.dumps({'error': 'Ejudge не отвечает :('})


@app.route('/personal/<int:ejid>')
def personal_result(ejid: int):
    try:
        table = get_table(load_results.TABLE_URL)
        parsed_table = parse_results(table)
        return get_personal_json(parsed_table, ejid)
    except ConnectionError:
        return json.dumps({'error': 'Ejudge не отвечает :('},
                           ensure_ascii=False)


@app.route('/personal/')
def personal():
    return render_template('personal.html')


if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)
    app.run("0.0.0.0", debug=True)
