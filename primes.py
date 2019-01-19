import math

def get_list_of_primes_up_to(num : int) -> list:
    '''Returns list of primes up to num'''

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
