from unittest import TestCase, skipUnless

from functions.math import TESTED, Math

__author__ = 'MKVJ48'
SKIP_MESSAGE = 'not_yet_implemented'


@skipUnless('fib' in TESTED, SKIP_MESSAGE)
class TestFib(TestCase):
    def test_fib_of_zero_is_zero(self):
        self.assertEqual(0, Math.fib(0))

    def test_fib_of_1_is_1(self):
        self.assertEqual(1, Math.fib(1))

    def test_fib_of_14_is_377(self):
        self.assertEqual(377, Math.fib(14))

    def test_fib_of_negative_numbers_is_zero(self):
        self.assertEqual(0, Math.fib(-50))


@skipUnless('fib_up_to' in TESTED, SKIP_MESSAGE)
class TestFibUpTo(TestCase):
    def test_fib_up_to_zero_is_list_with_zero(self):
        self.assertListEqual([0], Math.fib_up_to(0))

    def test_fib_up_to_1_is_list_with_zero_1_and_1(self):
        self.assertListEqual([0, 1, 1], Math.fib_up_to(1))

    def test_fib_up_to_5_is_list_with_zero_1_1_2_3_and_5(self):
        self.assertListEqual([0, 1, 1, 2, 3, 5], Math.fib_up_to(5))


@skipUnless('sign' in TESTED, SKIP_MESSAGE)
class TestSign(TestCase):
    def test_sign_of_minus_5_is_negative(self):
        self.assertEqual('negative', Math.sign(-5))

    def test_sign_of_5_is_positive(self):
        self.assertEqual('positive', Math.sign(5))

    def test_sign_of_zero_is_neutral(self):
        self.assertEqual('neutral', Math.sign(0))
