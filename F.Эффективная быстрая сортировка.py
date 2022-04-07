''' 
F.Эффективная быстрая сортировка

Формат ввода:
            В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
            В каждой из следующих n строк задана информация про одного из участников.
            i-й участник описывается тремя параметрами:
                                           - уникальным логином (строкой из маленьких латинских букв длиной не более 20);
                                           - числом решённых задач Pi;
                                           - штрафом Fi;
            Fi и Pi — целые числа, лежащие в диапазоне от 0 до 10^9.
            
Формат вывода:
             Для отсортированного списка участников выводится по порядку их логины по одному в строке.

Пример 1:
             Ввод:                    	Вывод:
             5                          gena
             alla 4 100                 timofey
             gena 6 1000                alla
             gosha 2 90                 gosha
             rita 2 90                  rita
             timofey 4 80
             
Пример 2:
             Ввод:	                    Вывод:
            5                           alla
            alla 0 0                    gena
            gena 0 0                    gosha
            gosha 0 0                   rita
            rita 0 0                    timofey
            timofey 0 0

'''


def effective_sort(array):
    def quick_sort(left, right):
        if right <= left:
            return array
        first, last = left, right
        pivot = (left + right) // 2
        reference = array[pivot]
        while first <= last:
            while array[first] < reference:
                first += 1
            while reference < array[last]:
                last -= 1
            if first <= last:
                array[first],array[last] = array[last], array[first]
                first += 1
                last -= 1
        quick_sort(left, last)
        quick_sort(first, right)
        return array
    return quick_sort(0, len(array) - 1)
        


if __name__ == '__main__':
    print( 
        *[name for _, _, name in effective_sort([ 
            (lambda name, points, penalty: 
                (-int(points), int(penalty), name)
            )(
                *input().split()
            ) for _ in range(int(input()))
        ])], 
        sep='\n',
    )  
