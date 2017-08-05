from flask import Flask
from flask.templating import render_template
import load_results
from load_results import (get_table_to_render, parse_results, get_table,
                          get_table_json)

app = Flask(__name__)


@app.route('/')
def index():
    table = get_table(load_results.TABLE_URL)
    parsed_table = parse_results(table)
    table_to_render = get_table_to_render(parsed_table)

    return render_template("index.html", table=table_to_render)


@app.route('/table')
def table():
    table = get_table(load_results.TABLE_URL)
    parsed_table = parse_results(table)
    return get_table_json(parsed_table)


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
