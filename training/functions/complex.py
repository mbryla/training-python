import os
import random

__author__ = 'mbryla'


def get_python_files(top_directory):
    files = list()

    for nodes in os.walk(top_directory):
        for file in nodes[2]:
            if file[-3:] == '.py':
                if file != '__init__.py':
                    files.append(file)

    return files


def may_raise_error():
    if random.random() > 0.6:
        raise ValueError("You're not lucky...")


def how_much_luck(n):
    data = {'lucky': 0, 'unlucky': 0}

    for i in range(0, n):
        try:
            may_raise_error()
            data['lucky'] += 1
        except ValueError:
            data['unlucky'] += 1

    return data
