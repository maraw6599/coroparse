#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

URL = 'https://www.worldometers.info/coronavirus/'

html = requests.get(URL).text
soup = BeautifulSoup(html, 'html.parser')

# TABLE#main_table_countries_today #main_table_countries_today TBODY
c_data = soup.select('TR[role="row"]')
print(c_data)