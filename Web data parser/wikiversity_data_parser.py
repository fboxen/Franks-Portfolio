"""This program gets the top 1000 most visited articles for each month within
the previous 12 months.

Input:
    Page view data file

Output:
    The top 100 total pages and learning projects by view
count in descending order.

References:
    * https://www.geeksforgeeks.org/python-urllib-module/#
    * https://stackoverflow.com/questions/20585920/how-to-add-multiple-values-to-a-dictionary-key
    * https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/#
    * https://www.geeksforgeeks.org/python-datetime-timedelta-function/
    * https://stackoverflow.com/questions/45117276/creating-a-dictionary-and-assigning-multiple-values-to-each-key-using-loops

Created by Frank Boxenbaum

"""

import json
import re
import urllib.request
import datetime


def get_dates():
    """Creates dictionary of past 12 months with corresponding year
    Args: None
    Returns:
        dates (dict): dictionary of past 12 months and corresponding years
    """

    dates = {}
    date = datetime.date.today()
    month = date.month
    year = date.year

    for _ in range(12):
        month -= 1
        if month == 0:
            month = 12
            year -= 1

        dates[month] = year

    return dates


def build_url(month, year):
    """Creates a url using the dates list
    Args:
        month (int): month
        year (int): year
    Returns:
        url (str): an API url
    """

    url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top" + \
        f"/en.wikiversity/all-access/{year}/{month:02}/all-days"

    return url


def get_webpage(url):
    """Gets the text of a given URL.
    Args:
        url (str): An API url to retrieve data from.
    Returns:
        data (string): The raw text of the web page.
    """

    data = urllib.request.urlopen(url).read().decode()

    return data


def create_dictionary(data):
    """Uses JSON to parse data and create a dictionary
    of page titles and view counts.
    Args:
        data (string): API dictionary to parse
    Returns:
        views (dictionary): a dictionary of page titles and view counts
    """
    views = {}

    jsdata = json.loads(data)
    for j in jsdata['items']:
        for item in j['articles']:
            views[item['article']] = int(item['views'])

    return views


def combine_dictionaries(views, all_views):
    """Combines the view counts and page titles of two dictionaries.
    Args:
        views (dictionary): a dictionary of page titles and view counts
        all_views (dictionary): a dictionary of page titles and view counts
    Returns:
        all_views (dictionary): a dictionary of page titles and view counts
    """

    for key, value in views.items():
        if key in all_views:
            all_views[key] += value
        else:
            all_views[key] = value

    return all_views


def parse_learning_group(all_views):
    """Uses regex to parse data and create a dictionary
    of learning groups and view counts.

    Args:
        views (dictionary): a dictionary of page titles and view counts

    Returns:
        groups (dictionary): a dictionary of page titles and view counts

    """

    groups = {}
    for item in all_views:
        learning = re.split(r'/|$', item)[0]
        counts = all_views[item]
        if learning not in groups.keys():
            groups[learning] = int(counts)
        else:
            groups[learning] += int(counts)

    return groups


def sort_data(views):
    """Sorts dictionary by descending sum of view counts.
    Args:
        views (dictionary): a dictionary of page titles and view counts
    Returns:
        result (list): a list of page titles view counts sorted by
        descending view counts
    """

    result = sorted(views.items(), key=lambda x: x[1], reverse=True)[:100]

    return result


def display_results(result, group_result):
    """Displays results of data parsing and sorting.

    Args:
        result (list): a list of page titles view counts sorted by
    descending view counts
        group_result (list): a list of page titles view counts sorted by
    descending view counts

    Returns: None

    """
    print('Page title : ' + 'Total view counts')
    print()
    for item in result:
        print(item[0], item[1])
    print()

    print('Learning Project : ' + 'Total view counts')
    print()
    for item in group_result:
        print(item[0], item[1])


def main():  # pragma: no cover
    """Runs the main program logic."""
    all_views = {}
    dates = get_dates()
    for month in dates:
        url = build_url(month, dates[month])
        data = get_webpage(url)
        views = create_dictionary(data)
        all_views = combine_dictionaries(views, all_views)

    groups = parse_learning_group(all_views)

    result = sort_data(all_views)
    group_result = sort_data(groups)
    display_results(result, group_result)


if __name__ == "__main__":  # pragma: no cover
    main()