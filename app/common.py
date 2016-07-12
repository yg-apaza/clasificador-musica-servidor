import json
import os


def load(var):
    # with open('settingsOpenshift.json') as data_file:
    with open(os.path.join(os.path.dirname(__file__),
                           'settings.json')) as data_file:
        data = json.load(data_file)
    if data[var]['type'] == 'env':
        return os.environ.get(data[var]['value'], '')
    elif data[var]['type'] == 'var':
        return data[var]['value']
    else:
        return ""
