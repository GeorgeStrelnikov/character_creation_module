from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(your_number):
    """Вычисляет квадратный корень."""
    return sqrt(your_number)


def calc(your_number):
    """Calculate square root."""
    root = calculate_square_root(your_number)
    if your_number <= 0:
        return 'root = 0'
    else:
        print(f'Мы вычислили квадратный корень из введённого вами числа. '
              f'Это будет: {root}')


calc(25.5)
