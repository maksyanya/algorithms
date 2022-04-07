''' 
D.Калькулятор

Формат ввода:
            В единственной строке дано выражение, записанное в обратной польской нотации. 
            Числа и арифметические операции записаны через пробел.
            На вход могут подаваться операции: +, -, *, / и числа, по модулю не превосходящие 10000.
            Гарантируется, что значение промежуточных выражений в тестовых данных по модулю не больше 50000.
            
Формат вывода:
            Выводится единственное число — значение выражения.
            
Пример 1:
            Ввод:       	 Вывод:
            2 1 + 3 *        9
            
Пример 2:
            Ввод:            Вывод:
            7 2 + 4 * 2 +    38

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
