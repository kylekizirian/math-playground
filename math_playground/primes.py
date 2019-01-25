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

    def __init__(self, number_of_primes):
        '''Generates a list of prime numbers with given length'''
        self._primes = [2, 3]

        count = 1
        while len(self._primes) < number_of_primes:
            # Check numbers of form 6n-1 and 6n+1 for primes
            next_potential_prime = 6 * count - 1
            if self.is_prime(next_potential_prime):
                self._primes.append(next_potential_prime)
            next_potential_prime += 2
            if self.is_prime(next_potential_prime):
                if len(self._primes) < number_of_primes:
                    self._primes.append(next_potential_prime)
            count += 1

    def __iter__(self):
        for prime in self._primes:
            yield prime

    def __contains__(self, item):
        return item in self._primes

    def __len__(self):
        return len(self._primes)

    def is_prime(self, potential_prime):
        '''TODO'''
        sqrt_potential_prime = potential_prime ** 0.5

        for prime in self._primes:
            if prime > sqrt_potential_prime:
                return True
            elif potential_prime % prime == 0:
                return False

        assert False, f'Needed more primes to determine if {potential_prime} is prime'

    def largest_prime(self):
        '''Returns largest prime number in list of primes
        
        >>> primes = Primes(10)
        >>> primes.largest_prime()
        29
        '''
        return self._primes[-1]
