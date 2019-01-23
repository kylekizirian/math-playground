import math


class Fibonacci():
    """Class for implementing fibonacci generator"""

    def __init__(self, fib_num):
        self.fib_num = fib_num
        self.second_last = 0
        self.last = 1

    def __iter__(self):

        yield self.last

        for _ in range(self.fib_num):
            next_fib_num = self.second_last + self.last
            self.second_last, self.last = self.last, next_fib_num
            yield next_fib_num


if __name__ == '__main__':

    fibonacci = Fibonacci(100)
    for index, fibonacci_num in enumerate(fibonacci, 1):
        print(f'Fib # {index:03} = {fibonacci_num:27,}')
