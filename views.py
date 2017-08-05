from flask import Flask
from flask.templating import render_template
import load_results
from load_results import parse_results, get_table, get_table_json
import json
from requests.exceptions import ConnectionError


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/table')
def table():
    try:
        table = get_table(load_results.TABLE_URL)
        parsed_table = parse_results(table)
        return get_table_json(parsed_table)
    except ConnectionError:
        return json.dumps({'error': 'Ejudge не отвечает :('})


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
