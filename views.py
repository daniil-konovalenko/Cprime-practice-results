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


@app.route('/table')
def table():
    try:
        table = get_table(load_results.TABLE_URL)
        parsed_table = parse_results(table)
        return get_table_json(parsed_table)
    except ConnectionError:
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

if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
