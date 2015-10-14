__author__ = 'MKVJ48'
TESTED = ['sign', 'fib', 'fib_up_to']


class Math:
    @staticmethod
    def sign(n):
        return 'positive' if n > 0 else 'negative' if n < 0 else 'neutral'

    @staticmethod
    def fib(n):
        a, b = 0, 1
        for i in range(0, n):
            a, b = b, a + b

        return a

    @staticmethod
    def fib_up_to(n):
        fibs = list()

        a, b = 0, 1
        while a <= n:
            fibs.append(a)
            a, b = b, a + b

        return fibs
