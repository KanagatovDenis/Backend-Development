def roman_to_int(roman):
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for index in range(len(roman)):
        current = numbers[roman[index]]

        if (index + 1 < len(roman)) and (current < numbers[roman[index + 1]]):
            total -= current
        else:
            total += current

    return total


def int_to_roman(number):
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
    ]
    result = ''

    for value, symbol in values:
        while number >= value:
            result += symbol
            number -= value

    return result


print('Добро пожаловать в римский конвертер!')

while True:
    operation = int(input('Введите 1 для перевода из римских цифр в арабские, иначе 2, и 0 для выхода: '))

    if operation == 0:
        print('Всего хорошего!')
        break
    elif operation == 1:
        print(roman_to_int(input('Введите число для преобразования: ')))
    elif operation == 2:
        print(int_to_roman(int(input('Введите число для преобразования: '))))
    else:
        print('Похоже, такой операции нет( введите повторно.')
