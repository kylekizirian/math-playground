from pymathutils import primes


def test_len_primes():
    primes_under_ten = primes.Primes(10)
    assert len(primes_under_ten) == 4


def test_in_primes():
    primes_under_ten = primes.Primes(10)
    assert 3 in primes_under_ten
    assert 4 not in primes_under_ten


def test_iter_primes():
    primes_under_ten = primes.Primes(10)
    primes_under_ten_list = [prime for prime in primes_under_ten]
    assert primes_under_ten_list == [2, 3, 5, 7]


def test_reversed_primes():
    primes_under_ten = primes.Primes(10)
    primes_under_ten_reversed = [prime for prime in reversed(primes_under_ten)]
    assert primes_under_ten_reversed == [7, 5, 3, 2]


def test_largest_prime():
    primes_under_thousand = primes.Primes(10 ** 3)
    largest_prime_under_thousand = primes_under_thousand.largest_prime()
    assert largest_prime_under_thousand == 997
