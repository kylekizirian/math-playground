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

    my_fib = Fibonacci(15)
    for index, fib_num in enumerate(my_fib):
        print(f'Fib # {index + 1:03} = {fib_num}')
