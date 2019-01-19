import math
import time


def simple_get_divisors(num : int) -> list:
    '''Returns a list of divisors of num from 1 to n / 2
    
    Uses simplest method by checking all numbers from 1 to n / 2 to determine
    if they are a divisor of n

    :param num: integer to get divisors of
    :return: list of divisors of num
    '''
    all_divisors = []
    for possible_divisor in range(1, math.floor(num / 2) + 1):
        if num % possible_divisor == 0:
            all_divisors.append(possible_divisor)
    return all_divisors


def get_divisors_parity_check(num : int) -> list:
    '''Returns a list of divisors of num from 1 to n / 2

    Slightly more sophisticated method of getting all divisors by checking if
    num is even and, if so, not considering even numbers as possible divisors
    
    :param num: integer to get divisors of
    :return: list of divisors of num
    '''
    all_divisors = []
    increment = 1
    # if number is odd, increment by 2 because don't have to check evens
    if num % 2 == 1:
        increment = 2

    for possible_divisor in range(1, math.floor(num / 2) + 1, increment):
        if num % possible_divisor == 0:
            all_divisors.append(possible_divisor)
    return all_divisors


def is_abundunt_num(num : int, get_divisors_func=simple_get_divisors) -> bool:
    '''Takes in an integer and returns whether it is an abundant numuber
    
    Finds all divisors between 1 and n / 2 and sums them up, determining
    if their sum is greater than n. If so, returns True, else False.

    :param num: number to check if abundant
    :return: bool
    '''
    divisors = get_divisors_func(num)
    return sum(divisors) > num


if __name__ == '__main__':
    
    range_to_check = 2 * 10**4

    start_time = time.time()
    for i in range(range_to_check):
        is_abundunt_num(i, simple_get_divisors)
    end_time = time.time()

    print(f'Simple check for all abundant numbers from 0 to {range_to_check} '
          f'took {end_time - start_time} seconds')

    start_time = time.time()
    for i in range(range_to_check):
        is_abundunt_num(i, get_divisors_parity_check)
    end_time = time.time()

    print(f'Check for all abundant numbers with parity from 0 to '
          f'{range_to_check} took {end_time - start_time} seconds')
