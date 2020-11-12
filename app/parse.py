from html.parser import HTMLParser

import requests
import requests.exceptions
from bs4 import BeautifulSoup
from pymysql import Connection

import config
from .exceptions import *


def parse(connection: Connection, day: str) -> list:
    """Get and parse source info file.
    """

    try:
        html = requests.get(config.URL).text
    except requests.exceptions.RequestException:
        raise NetworkException('Cannot get source file.')

    try:
        soup = BeautifulSoup(html, 'html.parser')
    except HTMLParser.HTMLParseError:
        raise FormatException('Cannot parse source file')

    c_data = soup.select(f'TABLE#main_table_countries_{day} TBODY TR')

    result = list()
    for row in c_data:
        if 'row_continent' in row.attrs.get('class', []):
            continue
        cells = [td.text.replace(',', '').strip() for td in row.select('td')]
        if not cells[0].strip():
            continue

        result.append(dict(zip(config.FIELDS, cells[1:])))

    return result
