'''
A. Ближайший ноль

Формат ввода:
            В первой строке дана длина улицы —– n (1 ≤ n ≤ 10^6).
            В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули).
            Гарантируется, что в последовательности есть хотя бы один ноль.
            Номера домов (положительные числа) уникальны и не превосходят 10^9.
            
            
Формат вывода: 
            Для каждого из участков выведите расстояние до ближайшего нуля.
            Числа выводите в одну строку, разделяя их пробелами.
            
Пример 1:
            Ввод:              Вывод:
            5                  0 1 2 1 0
            0 1 4 9 0
            
Пример 2:
            Ввод:              Вывод:
            6                  0 1 2 3 4 5
            0 7 9 4 8 20
            
'''


def finds_distanses_to_nearest_zero(houses, zero='0'):
    output = [0] * len(houses)
    zeros = [key for key, value in enumerate(houses) if value == zero]
    left = zeros[0]
    for position in range(0, left):
        output[position] = left - position
    for old, new in zip(zeros, zeros[1:]):
        for position in range(old, new):
            if position != old:
                output[position] = min(position - old, new - position)
    right = zeros[-1]
    for position in range(right + 1, len(houses)):
        output[position] = position - right
    return output


if __name__ == '__main__':
    input()
    print(*finds_distanses_to_nearest_zero(input().split()))
