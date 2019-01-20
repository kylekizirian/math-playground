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
