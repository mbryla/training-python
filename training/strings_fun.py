__author__ = 'MKVJ48'

FOX = 'The quick fox jumps over the lazy dog'


def ask_ok(prompt):
    value = input(prompt)

    if value in ('y', 'yes'):
        return True
    elif value in ('n', 'no'):
        return False
    else:
        raise ValueError('wrong!')


def custom_log(message, level='INFO', indent=4):
    print(' ' * indent + '{0} -> {1}'.format(level, message))
