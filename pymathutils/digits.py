'''Operations on digits'''


def num_digits(num: int) -> int:
    '''Returns number of digits in an integer
    
    >>> num_digits(123)
    3
    >>> num_digits(1)
    1
    >>> num_digits(-10)
    2
    '''
    return len(str(abs(num)))


def is_pandigital(num: int) -> bool:
    '''Returns whether a number is pandigital
    
    An n-digit number is pandigital if it makes use of
    all the digits 1 to n exactly once; for example, the 5-digit
    number, 15234, is 1 through 5 pandigital.

    >>> is_pandigital(2143)
    True
    >>> is_pandigital(2144)
    False
    >>> is_pandigital(210)
    False
    '''
    num_str: str = str(num)
    num_digits: int = len(num_str)

    if '0' in num_str:
        return False

    for n in num_str:
        if int(n) > num_digits:
            return False

    for i in range(1, num_digits):
        if num_str.count(str(i)) != 1:
            return False

    return True