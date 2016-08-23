from flask import Flask
from flask.templating import render_template
import load_results
from load_results import get_table_to_render, parse_table, get_table

app = Flask(__name__)


@app.route("/")
def index():
    table = get_table(load_results.TABLE_URL)
    parsed_table = parse_table(table)
    rendered_table = get_table_to_render(parsed_table)

    return render_template("index.html", table=rendered_table)


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
