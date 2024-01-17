"""
    Expected output:
    9 passed in 0.xx seconds
    References:
    * https://realpython.com/python-testing/
    * http://docs.pytest.org/en/latest/getting-started.html
"""

import os
import tempfile
import sqlite3
import pytest
import SQL_reader.py


def create_database():
    with tempfile.NamedTemporaryFile(prefix="database", suffix=".db", delete=False) as file:
        filename = file.name

    sql = """
        CREATE TABLE Test(
            id SERIAL,
            name VARCHAR
        );
        """
    query = "INSERT INTO test (name)" + \
        "VALUES ('Abel'), ('Cain');"

    with sqlite3.connect(filename) as connection:
        connection.execute(sql)
        connection.execute(query)

    return filename


def test_get_tables():
    filename = create_database()
    assert assignment_12.get_tables(filename) == [('Test',)]
    os.remove(filename)


def test_get_table_data():
    filename = create_database()
    user_table = 'Test'
    assert assignment_12.get_table_data(user_table, filename) == [(None, 'Abel'), (None, 'Cain')]
    os.remove(filename)


def test_get_fields():
    filename = create_database()
    user_table = 'Test'
    assert assignment_12.get_fields(user_table, filename) == {'id': 0, 'name': 1}
    os.remove(filename)


def test_get_max_length():
    filename = create_database()
    user_table = 'Test'
    columns = assignment_12.get_fields(user_table, filename)
    assert assignment_12.get_max_length(user_table, columns, filename) == {'id': None, 'name': 4}
    os.remove(filename)


def test_get_choice_returns_valid_input():
    tables = [('Regions',), ('Territories',), ('Suppliers',)]
    input_values = [1]

    def input(prompt=None):
        return input_values.pop()

    assignment_12.input = input
    assert assignment_12.get_choice(tables) == 1


def test_get_choice_returns_ignores_non_input():
    tables = [('Regions',), ('Territories',), ('Suppliers',)]
    input_values = ['one', 1]

    def input(prompt=None):
        return input_values.pop()

    assignment_12.input = input
    assert assignment_12.get_choice(tables) == 1


def test_get_choice_exits_on_enter():
    tables = [('Regions',), ('Territories',), ('Suppliers',)]
    input_values = ['']

    def input(prompt=None):
        return input_values.pop()

    with pytest.raises(SystemExit):
        assignment_12.input = input
        assignment_12.get_choice(tables)


def test_store_user_table():
    tables = [('Regions',), ('Territories',), ('Suppliers',)]
    assert assignment_12.store_user_table(tables, 1) == 'Regions'


def test_display_results(capsys):
    results = [(2, 'New Orleans Cajun Delights', 'Shelley Burke'), (3, "Grandma Kelly's Homestead", 'Regina Murphy'), (4, 'Tokyo Traders', 'Yoshi Nagase', 'Marketing Manager')]
    max_length = {'id': 2, 'company': 30, 'name': 10}
    assignment_12.display_results(results, max_length)
    captured = capsys.readouterr()
    assert "(2, \'New Orleans Cajun Delights\', \'Shelley Burke\')" in captured.out