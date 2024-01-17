"""
    Expected output:
    9 passed in 0.xx seconds
References:
    * https://realpython.com/python-testing/
    * http://docs.pytest.org/en/latest/getting-started.html
"""

import pytest
import wikiversity_data_parser


def test_get_dates_valid():
    result = assignment_11.get_dates()
    assert len(result) == 12
    for month in range(1, 13):
        assert month in result
        year = str(result[month])
        assert len(year) == 4 and year.isdigit()


def test_build_url_single():
    url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/' + \
          'en.wikiversity/all-access/2023/03/all-days'
    result = assignment_11.build_url(3, 2023)
    assert url == result


def test_build_url_valid():
    url = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/top/' + \
          'en.wikiversity/all-access/2022/10/all-days'
    result = assignment_11.build_url(10, 2022)
    assert url == result


def test_get_webpage():
    url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/top/" + \
           "en.wikiversity/all-access/2023/03/all-days"
    result = assignment_11.get_webpage(url)
    assert 'all-access' in result


def test_create_dictionary():
    data = '{"items":[{"project":"en.wikiversity","access":"all-access","year":"2022","month":"10","day":"all-days","articles":[{"article":"Wikiversity:Main_Page","views":147039,"rank":1},{"article":"Special:Search","views":38998,"rank":2}]}]}'
    result = assignment_11.create_dictionary(data)
    assert 'Wikiversity:Main_Page' in result
    assert result['Wikiversity:Main_Page'] == 147039


def test_combine_dictionaries_valid():
    views = {'Wireshark/Arp': 3, 'Wireshark/DHCP': 2, 'Wireshark/HTTP': 1}
    all_views = {'Wireshark/Arp': 5, 'Wireshark/DHCP': 1}
    result = assignment_11.combine_dictionaries(views, all_views)
    assert result == {
        'Wireshark/Arp': 8, 'Wireshark/DHCP': 3, 'Wireshark/HTTP': 1}


def test_parse_learning_group_valid():
    full_match = {'Wireshark/Arp': 8, 'Wireshark/DHCP': 3,
                  'Wireshark/HTTP': 2, 'YouTube': 1}
    assert assignment_11.parse_learning_group(full_match) == {'Wireshark': 13,
                                                              'YouTube': 1}


def test_sort_data():
    full_match = {'Wireshark/Arp': 8, 'Wireshark/DHCP': 3, 'Wireshark/HTTP': 1}
    result = assignment_11.sort_data(full_match)
    assert result == [
        ('Wireshark/Arp', 8),
        ('Wireshark/DHCP', 3),
        ('Wireshark/HTTP', 1)
    ]


def test_display_results(capsys):
    test = [
        ('Wireshark/Arp', 3),
        ('Wireshark/DHCP', 2),
        ('Wireshark/HTTP', 1)
    ]

    groups = [
        ('Wireshark/Brt', 8),
        ('Wireshark/DDP', 3),
        ('Wireshark/XYZ', 1)
    ]

    assignment_11.display_results(test, groups)
    captured = capsys.readouterr()
    assert "Wireshark/HTTP 1\n\nLearning Project : Total view" in captured.out