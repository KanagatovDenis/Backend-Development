from collections import Counter


def text_analysis():
    """Частотный анализ текста и вывод 3 частых символов"""
    s = input('Введите текст: ').lower()
    d = Counter(s)
    most_common_chars = d.most_common(3)

    for key, value in most_common_chars:
        print(f'Символ "{key}" встречается {value} раз')


text_analysis()
