import requests
import csv
from bs4 import BeautifulSoup


TOPICS_NUMBER = 6
LEVELS_NUMBER = 5
MIN_LEVEL_CONTEST_ID = "027713"
MAX_LEVEL_CONTEST_ID = "027717"
TABLE_URL = "https://ejudge.lksh.ru/standings/dk/stand.php?from={}&to={}&title=Зачет".format(MIN_LEVEL_CONTEST_ID,
                                                                                             MAX_LEVEL_CONTEST_ID)


# Fetches results table from ejudge
def get_table(table_url) -> BeautifulSoup:
    response = requests.get(table_url)
    soup = BeautifulSoup(response.text, "lxml")
    table = soup.select_one("table")
    return table


# Returns dict like {name: [1 if problem is solved else 0]}
def parse_table(table_soup: BeautifulSoup) -> dict:
    result = {}
    rows = [row for row in table_soup.select("tr") if row.has_attr("ejid")]
    for row in rows:
        group, last_name, first_name = row.select_one("nobr").contents[0].split()

        problem_tags = [td for td in row.findAll("td") if td.has_attr("title")]
        solved = [1 if tag["class"] == ["ac"] else 0 for tag in problem_tags]
        result[(group, last_name, first_name)] = solved

    return result


def calculate_mark(solved):
    levels = set()
    max_levels = []
    for topic in range(TOPICS_NUMBER):
        solved_from_topic = solved[topic::TOPICS_NUMBER]
        if any(solved_from_topic):
            max_level = list(reversed(solved_from_topic)).index(1)
            max_levels.append(max_level)

    max_levels.sort(reverse=True)
    for level in max_levels:
        while level in levels:
            level -= 1
        levels.add(level)

    return min(len(levels), len(max_levels))


def get_table_to_render(parsed_table: dict) -> list:
    return sorted([(*name, calculate_mark(solved)) for name, solved in parsed_table.items()])


if __name__ == '__main__':
    results_table = get_table(TABLE_URL)
    parsed_table = parse_table(results_table)
    table = get_table_to_render(parsed_table)
    with open("results.csv", "w", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(table)
