def find_nth_digit(n):
    """Функция нахождения N-ой цифры в последовательности 123456789101112..."""
    digit_length = 1
    count = 9
    start = 1

    while n > digit_length * count:
        n -= digit_length * count
        digit_length += 1
        count *= 10
        start *= 10

    num = start + (n - 1) // digit_length

    digit_index = (n - 1) % digit_length

    return int(str(num)[digit_index])


n = int(input('Введите позицию N: '))

print(f'Цифра на позиции {n}: {find_nth_digit(n)}')
