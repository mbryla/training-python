__author__ = 'MKVJ48'
TESTED = ['words_count', 'words_count_case_insensitive']


class Parse:
    @staticmethod
    def count_words(words, line):
        words_count = dict((word, 0) for word in words)

        for word in line.replace('.', '').replace(',', '').split(' '):
            if word in words_count.keys():
                words_count[word] += 1

        return words_count

    @staticmethod
    def count_words(words, line, case_sensitive=True):
        words_count = dict((word, 0) for word in words)

        for word in line.replace('.', '').replace(',', '').split(' '):
            if case_sensitive:
                if word in words_count.keys():
                    words_count[word] += 1
            else:
                for key in words_count.keys():
                    if word.upper() == key.upper():
                        words_count[key] += 1

        return words_count
