"""This program allows the user to access and display information from an
SQL database.

Input:
    SQL database file

Output:
    User requested SQL database table contents with column titles

References:
   * https://www.geeksforgeeks.org/how-to-list-tables-using-sqlite3-in-python/#
   * https://www.w3schools.com/sql/default.asp
   * https://stackoverflow.com/questions/9592287/retrieve-the-maximum-length-of-a-varchar-column-in-sql-server
   * https://www.peterbe.com/plog/how-to-pad-fill-string-by-variable-python


Created by Frank Boxenbaum

"""
import sqlite3


def get_tables(database):
    """Retrieves tables from an SQL database.

    Args:
        database (file): SQL database to retrieve tables from

    Returns:
        tables (list): list of SQL tables

    """

    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor.execute(query)
    tables = cursor.fetchall()
    cursor.close()
    connect.close()
    tables = list(tables)

    return tables


def get_choice(tables):
    """Displays menu and gets choice.

    Args:
        tables (list): list of SQL tables

    Returns:
        choice (int): represents the choice of the menu.

    """

    print()
    print("Select a table to display or press <enter> to quit:")
    while True:
        try:
            count = 0
            for item in tables:
                count += 1
                print(f"{count}: {item[0]}")

            choice = int(input())
            if 1 <= choice <= len(tables):
                return choice

        except ValueError:
            exit()


def store_user_table(tables, choice):
    """Stores the user selected table.

    Args:
        tables (list): list of SQL tables
        choice (int): represents the choice of the menu.

    Returns:
        user_Table (string): The user selected table as a formatted string

    """
    for item in tables:
        if (choice - 1) == tables.index(item):
            selection = tables[choice - 1]
            selection = str(selection).replace("(", "").replace(")", "")
            selection = selection.replace("'", "").replace(",", "")

    return selection


def get_table_data(user_table, database):
    """Gets the data from the the user selected table.

    Args:
        user_Table (string): The user selected table as a formatted string
        database (file): An SQL database

    Returns:
        results (list): List of table values.

    """
    results = []
    connect = sqlite3.connect(database)
    cursor = connect.cursor()
    query = "SELECT * FROM " + user_table + ";"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connect.close()
    results = list(results)

    return results


def get_fields(user_table, database):
    """Gets the field names for the user selected table.

    Args:
        user_Table (string): The user selected table as a formatted string
        database (file): An SQL database file

    Returns:
        columns (dictionary): Dictionary of table column names.

    """
    columns = {}
    column = 0
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    query = "SELECT * FROM " + user_table + ";"
    cursor.execute(query)
    for field in cursor.description:
        columns[field[0]] = column
        column = column + 1
    cursor.close()
    connection.close()

    return columns


def get_max_length(user_table, columns, database):
    """Gets the max length of field names for the user selected table.

    Args:
        user_Table (string): The user selected table as a formatted string
        columns (dictionary): Dictionary of table column names
        database (file): An SQL database file

    Returns:
        max_length (dictionary): Dictionary of field name max length values

    """
    max_length = columns
    connection = sqlite3.connect(database)
    for item in columns:
        cursor = connection.cursor()
        query = "SELECT MAX(LENGTH(" + item + ")) count FROM " + user_table
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            max_length[item] = row[0]

    cursor.close()
    connection.close()

    return max_length


def display_results(results, max_length):
    """Displays the results from the SQL query.

    Args:
        results (list): List of table values.
        max_length (dictionary): Dictionary of field name max length values

    Returns: None

    """
    print()
    for value in max_length.items():
        print(value[0].ljust(int(value[1]), ' '), end=" ")
    print()

    lengths = list(max_length.values())
    for row in results:
        index = 0
        for item in row:
            print(str(item).ljust(lengths[index], ' '), end=" ")
            index += 1
        print()


def main():  # pragma: no cover
    """Runs the main program logic."""
    database = "northwind.db"
    try:
        while True:
            tables = get_tables(database)
            choice = get_choice(tables)
            user_table = store_user_table(tables, choice)
            columns = get_fields(user_table, database)
            max_length = get_max_length(user_table, columns, database)
            results = get_table_data(user_table, database)
            display_results(results, max_length)
    except IOError:
        print('Unknown error has ocurred. Exiting')
        exit()


if __name__ == "__main__":  # pragma: no cover
    main()