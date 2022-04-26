import random


def randgen(x):
    """
    generating amount number of random numbers
    :param x: quantity of random numbers
    :return:
    """
    i = 0
    while i < x:
        i += 1
        yield random.randint(1, 100)


if __name__ == '__main__':
    for j in randgen(5):
        print(j)

    print([x for x in randgen(5)])
