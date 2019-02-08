import itertools
import math

import primes


def get_prime_factors(num: int, prime_list: list = None) -> list:
    """Returns a list of tuples containing prime factors and their multiplicty
    
    To speed up repeated calculations, can optionally pass in a list of primes
    which will be used to generate the list of prime factors.

    >>> get_prime_factors(12)
    [(2, 2), (3, 1)]
    >>> get_prime_factors(14)
    [(2, 1), (7, 1)]
    """
    upper_bound = math.ceil(num / 2) + 1
    if not prime_list:
        prime_list = [prime for prime in primes.Primes(upper_bound)]

    prime_factors = []
    for prime in prime_list:
        temp = num
        multiplicity = 0
        temp, remainder = divmod(temp, prime)
        while remainder == 0 and temp > 1:
            multiplicity += 1
            temp, remainder = divmod(temp, prime)
        if multiplicity > 0:
            prime_factors.append((prime, multiplicity))
        if prime > upper_bound:
            break

    return prime_factors


def simple_get_divisors(num: int) -> list:
    """Returns a list of proper divisors of num from 1 to n / 2
    
    Uses simplest method by checking all numbers from 1 to n / 2 to determine
    if they are a divisor of n

    >>> simple_get_divisors(21)
    [1, 3, 7]
    >>> simple_get_divisors(100)
    [1, 2, 4, 5, 10, 20, 25, 50]

    :param num: integer to get divisors of
    :return: list of proper divisors of num
    """
    all_divisors = []
    for possible_divisor in range(1, math.floor(num / 2) + 1):
        if num % possible_divisor == 0:
            all_divisors.append(possible_divisor)
    return all_divisors


def get_divisors_with_parity_check(num: int) -> list:
    """Returns a list of proper divisors of num from 1 to n / 2

    Slightly more sophisticated method of getting all divisors by checking if
    num is even and, if so, not considering even numbers as possible divisors

    >>> get_divisors_with_parity_check(21)
    [1, 3, 7]
    >>> get_divisors_with_parity_check(100)
    [1, 2, 4, 5, 10, 20, 25, 50]

    :param num: integer to get divisors of
    :return: list of proper divisors of num
    """
    all_divisors = []
    increment = 1
    # if number is odd, increment by 2 because don't have to check evens
    if num % 2 == 1:
        increment = 2

    for possible_divisor in range(1, math.floor(num / 2) + 1, increment):
        if num % possible_divisor == 0:
            all_divisors.append(possible_divisor)
    return all_divisors


def get_sum_of_proper_divisors(num: int, prime_factors: list = None) -> int:
    """Returns the sum of proper divisors of num
    
    Can optionally pass in a pre-calculated list of a num's prime factors
    where each list item is a tuple of the form (prime_factor, multiplicity)

    >>> get_sum_of_proper_divisors(14)
    10
    >>> get_sum_of_proper_divisors(24)
    36
    """
    if not prime_factors:
        prime_factors = get_prime_factors(num)

    sum_proper_divisors = 1
    for prime_factor, multiplicity in prime_factors:
        temp_sum = 0
        for i in range(multiplicity + 1):
            temp_sum += prime_factor ** i
        sum_proper_divisors *= temp_sum

    return sum_proper_divisors - num


def is_abundant_num(num: int, get_divisors_func=simple_get_divisors) -> bool:
    """Takes in an integer and returns whether it is an abundant numuber
    
    Finds all divisors between 1 and n / 2 and sums them up, determining
    if their sum is greater than n. If so, returns True, else False.

    >>> is_abundant_num(24)
    True
    >>> is_abundant_num(37)
    False
    >>> is_abundant_num(24, get_divisors_with_parity_check)
    True

    :param num: number to check if abundant
    :param get_divisors_func: function to use for getting num's divisors
    :return: bool
    """
    divisors = get_divisors_func(num)
    return sum(divisors) > num
