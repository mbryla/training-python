__author__ = 'mbryla'


def add_count_words(words_count, line, case_sensitive=True):
    for word in line.replace('.', '').replace(',', '').split(' '):
        if case_sensitive:
            if word in words_count.keys():
                words_count[word] += 1
        else:
            for key in words_count.keys():
                if word.upper() == key.upper():
                    words_count[key] += 1

    return words_count


def count_words_in_file(words, filename):
    words_count = dict((word, 0) for word in words)

    for line in open(filename):
        add_count_words(words_count, line)

    return words_count
