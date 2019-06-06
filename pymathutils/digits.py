"""Operations on digits"""
from typing import List, Tuple


def num_digits(num: int) -> int:
    """Returns number of digits in an integer

    >>> num_digits(123)
    3
    >>> num_digits(1)
    1
    >>> num_digits(-10)
    2
    """
    return len(str(abs(num)))


def share_digits(num1: int, num2: int) -> bool:
    """Returns whether num1 and num2 share any digits

    >>> share_digits(12, 25)
    True
    >>> share_digits(30, 21)
    False
    """
    num1_str, num2_str = str(num1), str(num2)
    for c in num1_str:
        if c in num2_str:
            return True

    return False


def shared_digits(num1: int, num2: int) -> List[int]:
    """Returns a list of digits in both num1 and num2

    Returns an empty list if no digits shared between two numbers.
    The list returned is unique, i.e. if digits appear multiple times
    in both numbers, it only appears once in the returned list.

    >>> shared_digits(123, 234)
    [2, 3]
    >>> shared_digits(123, 456)
    []
    """
    shared_d = [int(d) for d in str(num1) if d in str(num2)]
    return list(dict.fromkeys(shared_d))


def remove_shared_digits(num1: int, num2: int) -> Tuple[int, int]:
    """Takes two integers and returns them with shared digits removed

    If two integers don't share any digits, returns original numbers

    >>> remove_shared_digits(49, 98)
    (4, 8)
    >>> remove_shared_digits(12, 34)
    (12, 34)
    >>> remove_shared_digits(12, 22)
    (1, 0)
    """
    num1_str, num2_str = str(num1), str(num2)
    shared_d = shared_digits(num1, num2)
    for d in shared_d:
        num1_str = num1_str.replace(str(d), "")
        num2_str = num2_str.replace(str(d), "")
    if num1_str == "":
        num1_str = "0"
    if num2_str == "":
        num2_str = "0"
    return int(num1_str), int(num2_str)


def is_pandigital(num: int) -> bool:
    """Returns whether a number is pandigital

    An n-digit number is pandigital if it makes use of
    all the digits 1 to n exactly once; for example, the 5-digit
    number, 15234, is 1 through 5 pandigital.

    >>> is_pandigital(2143)
    True
    >>> is_pandigital(2133)
    False
    >>> is_pandigital(210)
    False
    """
    num_str: str = str(num)
    n_digits: int = len(num_str)

    if "0" in num_str:
        return False

    for n in num_str:
        if int(n) > n_digits:
            return False

    for i in range(1, n_digits):
        if num_str.count(str(i)) != 1:
            return False

    return True
