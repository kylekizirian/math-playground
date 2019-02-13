from math_playground import primes

def test_len_primes():
    primes_under_ten = primes.Primes(10)
    assert (len(primes_under_ten) == 4)

def test_in_primes():
    primes_under_ten = primes.Primes(10)
    assert (3 in primes_under_ten)
    assert (4 not in primes_under_ten)
