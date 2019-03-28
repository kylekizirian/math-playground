import math


class Fibonacci():
    """Class for implementing fibonacci generator
    
    >>> fibonacci_seq = Fibonacci(5)
    >>> for fibonacci_num in fibonacci_seq:
    ...     print(fibonacci_num)
    1
    1
    2
    3
    5
    """

    def __init__(self, fib_num):
        self.fib_num = fib_num
        self.second_last = 0
        self.last = 1

    def __iter__(self):

        yield self.last

        for _ in range(self.fib_num - 1):
            next_fib_num = self.second_last + self.last
            self.second_last, self.last = self.last, next_fib_num
            yield next_fib_num
