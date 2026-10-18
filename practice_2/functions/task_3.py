def print_pack_report(amount_of_cakes):
    for number in range(amount_of_cakes, 0, -1):
        if number % 15 == 0:
            print(f'{number} - расфасуем по 3 или по 5')
        elif number % 5 == 0:
            print(f'{number} - расфасуем по 5')
        elif number % 3 == 0:
            print(f'{number} - расфасуем по 3')
        else:
            print(f'{number} - не заказываем!')
