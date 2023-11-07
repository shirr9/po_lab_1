# Лабораторная ИСРПО
## Общее описание решения
- С помощью команды Git создала копию репозитория, который находится по ссылке
- Создала новую ветку с помощью команды git branch <new_f_409896> и переходим на соответствующую ветку с помощью команды git checkout <название ветки>
- Создала файл с помощью команды echo > rectangle.py – которая выводит сообщение (указывается перед >) в соответствующем
файле, и если его не существует - создает его
- Добавила файл rectangle.py в репозиторий с помощью команды git add text.txt
- Сделала коммит с помощью команды git commit -a -m "add rectangle.py"
- Аналогично создала и добавила файл triangle.py
- Исправила ошибку в вычислении периметра в файле rectangle.py
- Создала еще один коммит внутри этой же ветки, с сообщением о том, что была
исправлена ошибка
- Построила граф истории всего репозитория с однострочным выводом коммитов с помощью команды git log --oneline - которая позволяет посмотреть коммиты
(Graph чтобы вывелось в виде дерева, all чтобы вывелись все коммиты)
- Построила граф истории только текущей ветки с помощью команды git log --oneline - которая позволяет посмотреть коммиты ветки, на которой мы находимся
- Взяла хэши двух последних коммитов из истории и посмотрела,
какие изменения были внесены с помощью команды git show d8578ed – которая показывает изменения,
сделанные в заданном коммите
- Выполнила merge в ветку master с помощью команды git merge some_branch - которая позволяет замерджить some_branch в текущую ветку
- Сделала Pull Request с помощью команд:
git remote -v – управление удаленным репозиторием,
git remote set-url origin – задает URL репозитория,
git push -u origin main - устанавливает связь между той веткой, в которой мы находимся и
веткой main на удалённом сервере
- Удалила ветку <new_f_409896>
## Описание каждой функции с примерами вызова
~~~python
def area(r):
return math.pi * r * r
~~~
Принимает число r, возвращает площадь круга с радиусом r

example:


input: 1 

output: 3.141592653589793
~~~python
def perimeter(r):
    return 2 * math.pi * r
~~~
Принимает число r, возвращает длину окружности с радиусом r

example:


input: 1 

output 6.283185307179586
~~~python
def area(a, b):
    return a * b
~~~
Принимает числа a и b, возвращает площадь прямоугольника со сторонами a и b

example:


input: 2 3 

output: 6
~~~python
def perimeter(a, b):
    return (a + b)*2
~~~
Принимает числа a и b, возвращает периметр прямоугольника со сторонами a и b

example:


input: 2 3 

output: 10
~~~python
def area(a):
    return a * a
~~~
Принимает число a, возвращает площадь квадрата со стороной a

example:


input: 2

output: 4
~~~python perimeter(a):
return 4 * a
~~~
Принимает число a, возвращает периметр квадрата со стороной a

example:


input: 2

output: 8
~~~python
def area(a, h):
    return a * h / 2
~~~
Принимает числа a и h, возвращает площадь треугольника со стороной a и высотой h к этой стороне

example:


input: 3 4

output: 6
~~~python
def perimetr(a, b, c):
    return a + b + c
~~~
Принимает числа a,b,c, возвращает периметр треугольника со сторонами a,b,c

example:


input: 3 4 5

output: 12
## История изменения проекта с хешами комитов
- commit **76643bc0fd8521a99c21f37b7437d0b7aec65321**


Author: shirr9 <simkagaechka1@gmail.com>


Date:   Wed Sep 27 15:49:05 2023 +0300

    add new file
- commit **f08c26986e4fb9a16e65cc5658325cc85c814987 (origin/main, origin/HEAD)**

Author: shirr9 <simkagaechka1@gmail.com>


Date:   Sat Sep 23 14:26:28 2023 +0300

    fix bug
- commit **8302ee0a503a62ad20c00e4505dc15b3cf528ff9**

Author: shirr9 <simkagaechka1@gmail.com>


Date:   Sat Sep 23 14:12:24 2023 +0300

    add rectangle.py
- commit **d078c8d9ee6155f3cb0e577d28d337b791de28e2**

Author: smartiqa <info@smartiqa.ru>


Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added
- commit **8ba9aeb3cea847b63a91ac378a2a6db758682460**

Author: smartiqa <info@smartiqa.ru>


Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
