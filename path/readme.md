## BFS
В заданном лабиринте найти путь между двумя данными узлами. <br>
Метод решения: Поиск в глубину. <br>
Порядок просмотра узлов лабиринта 

       1 
       |
    3-- --4
       |
       2

# Файл исходных данных
Лабиринт. <br>
N - количество строк в лабиринте. <br>
M - количество столбцов в лабиринте. <br>

Далее построчно расположен сам лабиринт. <br>
Затем распологаются координаты источника и цели в формате X Y, где X - номер строки, Y - номер столбца. <br>
Кодировка лабиринта: 1 - запрет; 0 - свободно. <br>

#Пример. Для лабиринта

    11111
    10101 
    10001
    11111

файл данных должен быть следующим:

    4
    5
    1 1 1 1 1
    1 0 1 0 1
    1 0 0 0 1
    1 1 1 1 1
    2 2
    2 4
  
# Файл результатов
Маршрут в лабиринте. <br>
В случае отсутствия пути в файл результатов необходимо записать "N", при наличии пути "Y" и далее весь путь. <br>
Маршрут должен начинаться координатами источника и заканчиваться координатами цели. <br>
Каждый шаг записывается с новой строки в формате X Y, где X - номер строки, Y - номер столбца. <br>

Для примера, приведенного в описании файла исходных данных, файл результатов должен быть следующим :

    Y
    2 2
    3 2
    3 3
    3 4
    2 4