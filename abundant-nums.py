import math
import time


def simple_get_divisors(num : int) -> list:
    '''Returns a list of divisors of num from 1 to n / 2
    
    Uses simplest method by checking all numbers from 1
    to n / 2 to determine if they are a divisor of n
    '''
    all_divisors = []
    for possible_divisor in range(1, math.floor(num / 2) + 1):
        if num % possible_divisor == 0:
            all_divisors.append(possible_divisor)
    return all_divisors


def simple_is_abundunt_num(num : int) -> bool:
    '''Takes in an integer and returns whether it is an abundant numuber
    
    Finds all divisors between 1 and n / 2 and sums them up, determining
    if their sum is greater than n. If so, returns True, else False.

    :param num: number to check if abundant
    :return: bool
    '''
    divisors = simple_get_divisors(num)
    return sum(divisors) > num


if __name__ == '__main__':
    
    range_to_check = 10**4

    start_time = time.time()
    for i in range(range_to_check):
        simple_is_abundunt_num(i)
    end_time = time.time()

    print(f'Simple check for all abundant numbers from 0 to {range_to_check} '
          f'took {end_time - start_time} seconds')

