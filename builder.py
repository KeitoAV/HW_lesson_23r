from utils import *

CMD_TO_FUNCTION = {
    'filter': filter_query,
    'map': map_query,
    'unique': unique_query,
    'limit': limit_query,
    'sort': sort_query
}

FILE_NAME = 'data/apache_logs.txt'


def build_query(cmd, param, data):
    if data is None:
        with open(FILE_NAME) as file:
            prepared_data = list(map(lambda x: x.strip(), file))
    else:
        prepared_data = data

    return CMD_TO_FUNCTION[cmd](param=param, data=prepared_data)




