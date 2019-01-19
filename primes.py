import math


def get_list_of_primes_up_to(num: int) -> list:
    """Returns list of primes up to num

    >>> get_list_of_primes_up_to(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """

    all_primes = [2]
    for i in range(3, num, 2):
        upper_bound = math.sqrt(i)
        for prime in all_primes:
            if prime > upper_bound:
                all_primes.append(i)
                break
            if i % prime == 0:
                break
    return all_primes


def is_prime(num: int) -> bool:
    """Returns whether or not input num is prime
    
    >>> is_prime(17)
    True
    >>> is_prime(21)
    False
    """

    upper_bound = math.floor(math.sqrt(num))
    primes_up_to_upper_bound = get_list_of_primes_up_to(upper_bound)

    for prime in primes_up_to_upper_bound:
        if num % prime == 0:
            return False
    else:
        return True
