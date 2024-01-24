def is_even(number):
    match number:
        case 0: return True
        case -1: return False
        case _: return is_even(number - 2)


def main():
    number = int(input('Enter a number: '))
    print(f'{number} is {"even" if is_even(number) else "odd"}')


if __name__ == '__main__':
    main()
