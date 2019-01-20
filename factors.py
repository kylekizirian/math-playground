import math

import primes


def get_prime_factors(num: int, prime_list: list = None) -> list:
    """Returns a list of tuples containing prime factors and their frequency
    
    To speed up repeated calculations, can optionally pass in a list of primes
    which will be used to generate the list of prime factors.

    >>> get_prime_factors(12)
    [(2, 2), (3, 1)]
    >>> get_prime_factors(18)
    [(2, 1), (3, 2)]
    """

    upper_bound = math.ceil(math.sqrt(num))
    if not prime_list:
        prime_list = primes.get_list_of_primes_up_to(upper_bound)

    prime_factors = []
    for prime in prime_list:
        remainder = 0
        temp = num
        frequency = 0
        temp, remainder = divmod(temp, prime)
        while remainder == 0:
            frequency += 1
            temp, remainder = divmod(temp, prime)
        if frequency > 0:
            prime_factors.append((prime, frequency))
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
