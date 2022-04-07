''' 
D.Калькулятор


'''

import operator


OPERANDS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):   # добавляет элемент на вершину стека
        self.items.append(item)

    def pop(self):          # возвращает элемент с вершины стека и удаляет его
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError('stack is empty')
        

def calculating_by_polish(
    symbols,
    converter=int,
    stack=None,
    operands=OPERANDS):
    stack = Stack() if stack is None else stack
    for value in symbols:
        if value in operands:
            operand1, operand2 = stack.pop(), stack.pop()
            stack.push(operands.get(value)(operand2, operand1))
        else:
            try:
                stack.push(converter(value))
            except ValueError:
                print(f'unable to convert {value} in {convert.__name__}' )
    return stack.pop()


if __name__ == '__main__':
    print(calculating_by_polish(input().split(' ')))
