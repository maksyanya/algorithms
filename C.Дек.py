'''
C.Дек

Формат ввода:
            В первой строке записано количество команд n — целое число, не превосходящее 100000. 
            Во второй строке записано число m — максимальный размер дека. Он не превосходит 50000.
            В следующих n строках записана одна из команд:
                   - push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, выводится «error»;
                   - push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error»;
                   - pop_front() – выводится первый элемент дека и удаляет его. Если дек был пуст, то выводится «error»;
                   - pop_back() – выводится последний элемент дека и удаляет его. Если дек был пуст, то выводится «error»;
            Value — целое число, по модулю не превосходящее 1000.


Формат вывода:
            Выводится результат выполнения каждой команды на отдельной строке. 
            Для успешных запросов push_back(x) и push_front(x) ничего не выводится.
            
Пример 1:
            Ввод:               	Вывод:
            4                     861
            4                     -819
            push_front 861
            push_front -819
            pop_back
            pop_back

Пример 2:
            Ввод:               	Вывод:
            7                     -855
            10                    0
            push_front -855       844
            push_front 0
            pop_back
            pop_back
            push_back 844
            pop_back
            push_back 823


Пример 3:
            Ввод:               	Вывод:
            6                     20
            6                     102
            push_front -201
            push_back 959
            push_back 102
            push_front 20
            pop_front
            pop_back

'''


class EmptyItemsException(Exception):
        pass


class FullItemsException(Exception):
        pass


class Deque:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size 
        self.head = 0
        self.tail = -1
        self.size = 0

    @property
    def is_empty(self):
        return self.size == 0
        
    @property
    def is_full(self):
        return self.size == self.max_size
        
    def push_back(self, item):  # вставка нового элемента в конец
        if self.is_full:
            raise FullItemsException('deque is full')
        self.tail = (self.tail + 1) % self.max_size
        self.items[self.tail] = item
        self.size += 1
        
    def pop_back(self):         # удаление последнего элемента
        if self.is_empty:
            raise EmptyItemsException('deque is empty')
        item = self.items[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return item
        
    def push_front(self, item): # вставка нового элемента в начало
        if self.is_full:
            raise FullItemsException('deque is full')
        self.head = (self.head - 1) % self.max_size
        self.items[self.head] = item
        self.size += 1
        
    def pop_front(self):        # удаление первого элемента
        if self.is_empty:
            raise EmptyItemsException('deque is empty')
        item = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item
        
    def size(self):             # количество элементов в очереди
        return len(self.items)

    def __str__(self):      
        return str(self.items)


if __name__ == "__main__":
    commands_number = int(input())
    deque = Deque(int(input()))

    for _ in range(commands_number):
        try:
            command, *numbers = input().split()
            try:
                result = getattr(deque, command)(*numbers)
            except AttributeError:
                print(f'"{command}" - unable data that stopped the work')
            if result is not None:
                print(result)
        except (EmptyItemsException, FullItemsException):
            print('error')
