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


if __name__ == "__main__":

    range_to_check = 2 * 10 ** 3

    start_time = time.time()
    num_abundant_numbers = 0
    for i in range(2, range_to_check):
        if is_abundunt_num(i, factors.simple_get_divisors):
            num_abundant_numbers += 1
    end_time = time.time()

    print(
        f"Simple check for all abundant numbers from 0 to {range_to_check} "
        f"took {end_time - start_time} seconds. Found {num_abundant_numbers} "
        f"abundant numbers"
    )

    start_time = time.time()
    num_abundant_numbers = 0
    for i in range(2, range_to_check):
        if is_abundunt_num(i, factors.get_divisors_with_parity_check):
            num_abundant_numbers += 1
    end_time = time.time()

    print(
        f"Check for all abundant numbers with parity from 0 to "
        f"{range_to_check} took {end_time - start_time} seconds. "
        f"Found {num_abundant_numbers} abundant numbers"
    )

    start_time = time.time()
    num_abundant_numbers = 0
    for i in range(2, range_to_check):
        prime_factors = factors.get_prime_factors(i)
        if factors.get_sum_of_proper_divisors(i, prime_factors) > i:
            num_abundant_numbers += 1
    end_time = time.time()

    print(
        f"Check for all abundant numbers with sum proper divisors from 0 to "
        f"{range_to_check} took {end_time - start_time} seconds. Found "
        f"{num_abundant_numbers} abundant numbers"
    )