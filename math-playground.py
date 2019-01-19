import math


def is_abundunt_num(num : int) -> bool:
    '''Takes in an integer and returns whether it is an abundant numuber
    
    Finds all divisors between 1 and n / 2 and sums them up, determining
    if their sum is greater than n. If so, returns True, else False.

    :param num: number to check if abundant
    :return: bool
    '''

    assert isinstance(num, int) and num > 2, ('Input must be an int greater '
                                              'than 2')

    divisors = []
    for i in range(1, math.floor(num / 2) + 1):
        if num % i == 0:
            divisors.append(i)

    return sum(divisors) > num


if __name__ == '__main__':
    pass
