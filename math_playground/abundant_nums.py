import math
import time

import factors


def is_abundant_num(num: int, get_divisors_func=factors.simple_get_divisors) -> bool:
    """Takes in an integer and returns whether it is an abundant numuber
    
    Finds all divisors between 1 and n / 2 and sums them up, determining
    if their sum is greater than n. If so, returns True, else False.

    >>> is_abundant_num(24)
    True
    >>> is_abundant_num(37)
    False
    >>> is_abundant_num(24, factors.get_divisors_with_parity_check)
    True

    :param num: number to check if abundant
    :param get_divisors_func: function to use for getting num's divisors
    :return: bool
    """
    divisors = get_divisors_func(num)
    return sum(divisors) > num
