RU_ALPHABET, EN_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "abcdefghijklmnopqrstuvwxyz"


def detect_language(text):
    ru_counter, en_counter = 0, 0

    for char in text:
        lower_char = char.lower()

        if lower_char in RU_ALPHABET:
            ru_counter += 1
        elif lower_char in EN_ALPHABET:
            en_counter += 1

    return 'ru' if ru_counter > en_counter else 'en'


def shift_char(char, shift, alphabet):
    lower_char = char.lower()

    if lower_char not in alphabet:
        return char

    position = alphabet.index(lower_char)
    new_position = (position + shift) % len(alphabet)
    shifted_char = alphabet[new_position]

    if char.isupper():
        return shifted_char.upper()

    return shifted_char


def encrypt(text, shift):
    language = detect_language(text)
    shifted_text = ''

    if language == 'ru':
        for char in text:
            shifted_char = shift_char(char, shift, RU_ALPHABET)
            shifted_text += shifted_char
    else:
        for char in text:
            shifted_char = shift_char(char, shift, EN_ALPHABET)
            shifted_text += shifted_char

    return shifted_text


def decrypt(text, shift):
    shifted_text = encrypt(text, shift * (-1))

    return shifted_text


while True:
    operation = int(input('Здравствуйте! Введите 1 (шифрофка), 2 (дешифровка) и 0 (выход из программы): '))

    if operation == 0:
        print('Всего хорошего!')
        break

    if operation == 1:
        text = input('Введите текст для изменения: ')
        shift = int(input('Введите шаг для сдвига: '))

        result = encrypt(text, shift)

        print(f'Итоговая строка: {result}')
    elif operation == 2:
        text = input('Введите текст для изменения: ')
        shift = int(input('Введите шаг для сдвига: '))

        result = decrypt(text, shift)

        print(f'Итоговая строка: {result}')
    else:
        print('Похоже, вы неверно ввели цифру операции. Попробуйте заново')
