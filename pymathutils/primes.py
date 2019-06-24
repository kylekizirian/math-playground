import math


class Primes:
    """Class that generates primes up to specified number

    Uses Sieve of Eratosthenes to generate the list of primes

    >>> primes = Primes(20)
    >>> [prime for prime in primes]
    [2, 3, 5, 7, 11, 13, 17, 19]
    """

    def __init__(self, up_to: int):
        """Generates a list of prime numbers up to given number

        >>> primes = Primes(10)
        >>> for prime in primes:
        ...    print(prime)
        2
        3
        5
        7
        """
        self._sieve = [True] * (up_to + 1)
        self._sieve[:2] = [False] * 2  # mark 0 and 1 not prime
        for index, prime in enumerate(self._sieve):
            if not prime:
                continue
            if index > math.ceil(up_to // 2):
                break
            for non_prime in range(index * 2, up_to + 1, index):
                self._sieve[non_prime] = False
        self._prime_list = [index for index, prime in enumerate(self._sieve) if prime]
        self._prime_set = set(self._prime_list)
        self._len = len(self._prime_set)

    def __iter__(self):
        """ Iterate over prime numbers
        >>> primes = Primes(8)
        >>> for prime in primes:
        ...     print(prime)
        2
        3
        5
        7
        """
        for prime in self._prime_list:
            yield prime

    def __reversed__(self):
        """ Iterate over primes starting at end
        >>> primes = Primes(8)
        >>> for prime in reversed(primes):
        ...     print(prime)
        7
        5
        3
        2
        """
        for prime in reversed(self._prime_list):
            yield prime

    def __contains__(self, item: int):
        """Returns whether given number is prime

        >>> primes = Primes(50)
        >>> 7 in primes
        True
        >>> 8 in primes
        False
        """
        return item in self._prime_set

    def __len__(self):
        """Gets number of primes in object

        >>> primes = Primes(50)
        >>> len(primes)
        15
        """
        return self._len

    def __getitem__(self, pos):
        """Gets prime at position

        >>> primes = Primes(50)
        >>> primes[0]
        2
        >>> primes[0:4]
        [2, 3, 5, 7]
        """
        return self._prime_list[pos]

    def is_prime(self, potential_prime: int) -> bool:
        """Checks if a given input number is prime

        >>> primes = Primes(100)
        >>> primes.is_prime(11)
        True
        >>> primes.is_prime(12)
        False
        """
        return potential_prime in self

    def largest_prime(self) -> int:
        """Returns largest prime number in list of primes

        >>> primes = Primes(30)
        >>> primes.largest_prime()
        29
        """
        return self._prime_list[-1]
