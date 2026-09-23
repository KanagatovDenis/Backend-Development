def sieve_of_eratosthenes(n):
    """Решето Эратосфена для поиска простых чисел до N"""
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]


def find_prime_divisor():
    """Вывод всех простых чисел из диапазона [2, N]"""
    num = int(input('Введите натуральное число: '))

    prime_numbers = sieve_of_eratosthenes(num)
    print(f'Все простые числа в диапазоне [2, {num}]:', ', '.join(map(str, prime_numbers)))


find_prime_divisor()
