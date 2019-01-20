import math
import time

import factors


def is_abundunt_num(num: int, get_divisors_func=factors.simple_get_divisors) -> bool:
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


if __name__ == "__main__":

    range_to_check = 2 * 10 ** 4

    start_time = time.time()
    for i in range(range_to_check):
        is_abundunt_num(i, factors.simple_get_divisors)
    end_time = time.time()

    print(
        f"Simple check for all abundant numbers from 0 to {range_to_check} "
        f"took {end_time - start_time} seconds"
    )

    start_time = time.time()
    for i in range(range_to_check):
        is_abundunt_num(i, factors.get_divisors_with_parity_check)
    end_time = time.time()

    print(
        f"Check for all abundant numbers with parity from 0 to "
        f"{range_to_check} took {end_time - start_time} seconds"
    )
