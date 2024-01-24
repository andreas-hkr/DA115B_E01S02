def map(func, iterable):
    return [func(item) for item in iterable]


def filter(func, iterable):
    return [item for item in iterable if func(item)]


def add(factor):
    def add_number(value):
        return factor + value

    return add_number


def is_even(number):
    return number % 2 == 0


def main():
    add_three = add(3)
    numbers = [1, 2, 3, 4, 5]

    print(map(add_three, numbers))
    print(filter(is_even, map(add_three, numbers)))


if __name__ == '__main__':
    main()
