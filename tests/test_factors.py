from hypothesis import given, settings, strategies

from pymathutils import factors


@given(strategies.integers(min_value=1, max_value=10 ** 6))
@settings(deadline=None)
def test_get_prime_factors(num):
    prime_factors = factors.get_prime_factors(num)
    result = 1
    for prime_factor in prime_factors:
        result *= prime_factor[0] ** prime_factor[1]
    assert result == num
