import sys

__author__ = 'mbryla'


def read_requirements_file(filename):
    """
    :param filename: filename.txt with requirements
    :return: single string with all the contents of the file with newlines removed
    """

    # hint: f.readlines() and ''.join(list)
    return ''


def extract_requirements(requirements_string):
    """
    :param requirements_string: single string with requirements
    :return: list of requirements in form ('SRS ID', 'Release', 'Feature', 'Object Type')
    """

    # hint: regex
    return []


def store_as_json(requirements_list, filename):
    """
    :param requirements_list: list of requirements in form ('SRS ID', 'Release', 'Feature', 'Object Type')
    :param filename: filename.json to store data
    """

    # hint: json.dumps
    pass


def store_as_csv(requirements_list, filename):
    """
    :param requirements_list: list of requirements in form ('SRS ID', 'Release', 'Feature', 'Object Type')
    :param filename: filename.csv to store data
    """

    # hint: maybe you should remove commas from requirements_string in extract_requirements?
    pass


if __name__ == '__main__':
    if len(sys.argv) == 2:
        requirements_string = read_requirements_file(sys.argv[1])
        requirements = extract_requirements(requirements_string)
        store_as_json(requirements, sys.argv[1] + '.json')
        store_as_csv(requirements, sys.argv[1] + '.csv')
    else:
        print('Usage: requirements.py requirements_file.txt')