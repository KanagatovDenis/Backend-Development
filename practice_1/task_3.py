from random import choice, shuffle
from string import ascii_uppercase as letters, digits


def create_password():
    """Генератор паролей по заданным параметрам"""
    random_letters = [choice(letters) for _ in range(3)]
    random_digits = [choice(digits) for _ in range(3)]
    random_specials = [choice('(!@#$%^&*') for _ in range(2)]

    password = random_letters + random_digits + random_specials
    shuffle(password)

    print(''.join(password))


create_password()
