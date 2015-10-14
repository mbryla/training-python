from unittest import TestCase, skipUnless

from functions.parse import TESTED, Parse

__author__ = 'MKVJ48'
SKIP_MESSAGE = 'not_yet_implemented'


@skipUnless('words_count' in TESTED, SKIP_MESSAGE)
class TestWordsCount(TestCase):
    def test_words_count_simple(self):
        line = 'To Sherlock Holmes she is always the woman'
        words = ['Sherlock', 'woman']

        self.assertDictEqual({'Sherlock': 1, 'woman': 1}, Parse.count_words(words, line))

    def test_words_count_simple_with_dot(self):
        line = ('I have seldom heard him mention her under any other name.'
                'In his eyes she eclipses and predominates the whole of he'
                'r sex. It was not that he felt any emotion akin to love f'
                'or Irene Adler. All emotions, and that one particularly, '
                'were abhorrent to his cold, precise but admirably balance'
                'd mind.')
        words = ['and', 'her', 'Irene']

        self.assertDictEqual({'and': 2, 'her': 2, 'Irene': 1}, Parse.count_words(words, line))


@skipUnless('words_count_case_insensitive' in TESTED, SKIP_MESSAGE)
class TestWordsCountCaseSensitive(TestCase):
    def test_words_count_simple(self):
        line = 'To Sherlock Holmes she is always the woman'
        words = ['sherlock', 'woman']

        self.assertDictEqual({'sherlock': 1, 'woman': 1}, Parse.count_words(words, line, False))

    def test_words_count_simple_with_dot(self):
        line = ('I have seldom heard him mention her under any other name.'
                'In his eyes she eclipses and predominates the whole of he'
                'r sex. It was not that he felt any emotion akin to love f'
                'or Irene Adler. All emotions, and that one particularly, '
                'were abhorrent to his cold, precise but admirably balance'
                'd mind.')
        words = ['and', 'Her', 'irene']

        self.assertDictEqual({'and': 2, 'Her': 2, 'irene': 1}, Parse.count_words(words, line, False))
