def temperature_converter():
    """Функция перевода температуры в градусах Цельсия в градусы Фаренгейта и Кельвина"""
    celcius = float(input('Введите температуру в Цельсиях: '))

    fahrenheit = (celcius * 9 / 5) + 32
    kelvin = celcius + 273.15

    print(f'{celcius}°C = {fahrenheit:.2f}°F')
    print(f'{celcius}°C = {kelvin:.2f}°K')


temperature_converter()
