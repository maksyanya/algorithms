'''A. Ближайший ноль. '''

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

