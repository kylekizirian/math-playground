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

    upper_bound = math.ceil(math.sqrt(num))
    primes_up_to_upper_bound = get_list_of_primes_up_to(upper_bound)

    for prime in primes_up_to_upper_bound:
        if num % prime == 0:
            return False
    else:
        return True


class Primes:

    def __init__(self, up_to: int):
        '''Generates a list of prime numbers up to given number

        >>> primes = Primes(10)
        >>> for prime in primes:
        ...    print(prime)
        2
        3
        5
        7
        '''
        #self._primes = [2, 3]
        self._sieve = [True] * (up_to + 1)
        self._sieve[0] = False
        self._sieve[1] = False
        for index, truth in enumerate(self._sieve):
            if not truth:
                continue
            if index > math.ceil(up_to // 2):
                break
            ii = index * 2
            while ii < up_to + 1:
                self._sieve[ii] = False
                ii += index

    def __iter__(self):
        ''' Iterate over prime numbers
        >>> primes = Primes(8)
        >>> for prime in primes:
        ...     print(prime)
        2
        3
        5
        7
        '''
        for index, is_prime in enumerate(self._sieve):
            if is_prime:
                yield index

    def __contains__(self, item: int):
        '''Returns whether given number is prime
        
        >>> primes = Primes(50)
        >>> 7 in primes
        True
        >>> 8 in primes
        False
        '''
        return self._sieve[item]

    def __len__(self):
        '''Gets number of primes up in object

        >>> primes = Primes(50)
        >>> len(primes)
        15
        '''
        return len([prime for prime in self._sieve if prime])

    def is_prime(self, potential_prime: int) -> bool:
        '''Checks if a given input number is prime

        >>> primes = Primes(100)
        >>> primes.is_prime(11)
        True
        >>> primes.is_prime(12)
        False
        '''
        return potential_prime in self

    def largest_prime(self) -> int:
        '''Returns largest prime number in list of primes

        >>> primes = Primes(30)
        >>> primes.largest_prime()
        29
        '''
        for index, is_prime in reversed(list(enumerate(self._sieve))):
            if is_prime:
                return index
