from flask import Flask
from flask.templating import render_template
import requests
from bs4 import BeautifulSoup
from load_results import get_table_to_render, TABLE_URL, parse_table

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get(TABLE_URL)

    soup = BeautifulSoup(response.text, "lxml")
    table = soup.select_one("table")
    parsed_table = parse_table(table)
    table = get_table_to_render(parsed_table)

    return render_template("index.html", table=table)


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
