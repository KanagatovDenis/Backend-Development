from string import ascii_lowercase, ascii_uppercase, digits
import secrets

SPECIAL_SYMBOLS = '!@#$%;:,./|-_+=^&*?'


def password_generator():
    print('Здравствуйте! Это генератор паролей с возможностью настройки параметров пароля. Приступим')

    is_lower_needed = int(input('Введите 1, если пароль должен содержать символы в нижнем регистре, иначе 0: '))
    is_upper_needed = int(input('Введите 1, если пароль должен содержать символы в верхнем регистре, иначе 0: '))
    is_specials_needed = int(input('Введите 1, если пароль должен содержать спецсимволы, иначе 0: '))
    is_digits_needed = int(input('Введите 1, если пароль должен содержать цифры, иначе 0: '))
    password_length = int(input('Введите длину пароля: '))

    pools = []

    if is_lower_needed:
        pools.append(ascii_lowercase)
    if is_upper_needed:
        pools.append(ascii_uppercase)
    if is_specials_needed:
        pools.append(SPECIAL_SYMBOLS)
    if is_digits_needed:
        pools.append(digits)

    if not pools:
        raise ValueError('Выберите хотя бы один тип символов.')
    if password_length < len(pools):
        raise ValueError(
            f'Длина должна быть не меньше {len(pools)}, чтобы в пароле были все выбранные типы символов.'
        )

    all_symbols = ''.join(pools)

    password = [secrets.choice(pool) for pool in pools]

    while len(password) < password_length:
        password.append(secrets.choice(all_symbols))

    secrets.SystemRandom().shuffle(password)

    print(f'Ваш пароль: {"".join(password)}')
