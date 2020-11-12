#!/usr/bin/env python
import json

import pymysql.cursors
import datetime
from pymysql import MySQLError

import config

from app.parse import parse, CoroparseException


def main():
    try:
        connection = pymysql.connect(
            host=config.MYSQL_HOST,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            db=config.MYSQL_DB,
            cursorclass=pymysql.cursors.DictCursor
        )
    except MySQLError as e:
        print(f'MySWL error: {e}')
        exit(0)

    date = datetime.datetime.utcnow()

    for day in config.DAYS:
        print(f'process {day}')
        with open(f'out-{date.strftime("%Y-%m-%d")}.json', 'wt') as out:
            try:
                data = parse(connection, day)
                out.write(json.dumps(data, indent=4))
            except CoroparseException as e:
                print(f'Error "{type(e)}": {e}')
            except IOError as e:
                print(f'Error "{type(e)}": {e}')

        date -= datetime.timedelta(days=1)


if __name__ == '__main__':
    main()
