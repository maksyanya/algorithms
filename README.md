# Алгоритмы и структуры данных

## Алгоритмы
#### [A.Ближайший ноль:](https://github.com/maksyanya/algorithms/blob/main/A.%D0%91%D0%BB%D0%B8%D0%B6%D0%B0%D0%B9%D1%88%D0%B8%D0%B9%20%D0%BD%D0%BE%D0%BB%D1%8C.py)
###### Улица, на которой хочет жить Тимофей, имеет длину n, то есть состоит из n одинаковых идущих подряд участков. На каждом участке либо уже построен дом, либо участок пустой. Тимофей ищет место для строительства своего дома. Он очень общителен и не хочет жить далеко от других людей, живущих на этой улице. 
###### Чтобы оптимально выбрать место для строительства, Тимофей хочет для каждого участка знать расстояние до ближайшего пустого участка. (Для пустого участка эта величина будет равна нулю –— расстояние до самого себя). 
###### Задача –— помочь Тимофею посчитать искомые расстояния. Для этого есть карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.
#### [B.Ловкость рук:](https://github.com/maksyanya/algorithms/blob/main/B.%D0%9B%D0%BE%D0%B2%D0%BA%D0%BE%D1%81%D1%82%D1%8C%20%D1%80%D1%83%D0%BA.py)
###### Гоша и Тимофей нашли необычный тренажёр для скоростной печати и хотят освоить его. Тренажёр представляет собой поле из клавиш 4× 4, в котором на каждом раунде появляется конфигурация цифр и точек. На клавише написана либо точка, либо цифра от 1 до 9. В момент времени t игрок должен одновременно нажать на все клавиши, на которых написана цифра t. 
###### Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый. Если в момент времени t были нажаты все нужные клавиши, то игроки получают 1 балл.
###### Задача –— найти число баллов, которое смогут заработать Гоша и Тимофей, если будут нажимать на клавиши вдвоём.
![image](https://github.com/maksyanya/algorithms/blob/main/images/image.png)
## Структуры данных
#### [C.Дек:](https://github.com/maksyanya/algorithms/blob/main/C.%D0%94%D0%B5%D0%BA.py)
###### Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом. Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много элементов, программа работала очень долго. Дело в том, что не все операции выполнялись за O(1).  
###### Задача –— написать эффективную реализацию.


## Рекурсия и сортировки
