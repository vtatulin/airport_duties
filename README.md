# airport_duties

Смены и работники

## Условие

Дан график получасовых срезов, заданный массивом. Индекс-номер смены, значение - требуемое количество человек.
В одну смену можно ставить одного человека, продолжительность смены - не менее 4 получасовых срезов. 
Вариант: не менее 4 часов, т.е. 8 срезов.
Найти оптимальное расписание смен.

## Решение.

Построим график в виде ступенек. 
Надо заполнить площадь под графиком полосками смен длинной от 4 и больше.
Попробуем решить эту задачу как задачу раскроя материала.
Определим объект "смена каботника"
свойства:
"номер начальной смены"
"продолжительность смены"
"высота" на графике. первоначально планировалось только для удобства визуализации, 
а потом выяснилось, что у этого свойства есть смысл для логики объединения смен.



а) заполним всю площадь под графиком сменами работников необходимой для заполнения длинны
б) наложим условие "смена длинной не менее 4" на все смены, кроме последней в ряду
в) обеъдиним смены, если они накладываются
г) наложим условие  "смена длинной не менее 4" на все смены


Пункт В оказался самым сложным: требовалось пересечь массив отрезков оптимально (не за квадратичное количество итераций), не ошибиться в геометрическом смысле объектов.
Пришлось делать по методике "разработка через тестирование"

## Оценка решения
Насколько оптимально расколожение смен? Оптимальнее всего, чтобы количество оплаченных человеко-часов было равно количеству требуемых человеко-часов.
Первая веичина считается суммой всех длительностей смен. Вторая суть площадь под графиком.

Если поставить условие "минимальная длинна смены = 1", то решение будет идеальным, количество оплаченных человеко-часов равно количеству затребованных.
Условие "минимальная длинна смены" добавляет переплату, делает решение неоптимальным.

## Как пользоваться
Запустить скрипт "main.py", посмотреть на графики.
Провариировать график срезов на входе алгоритма, снова посмотреть на графики.
Вровариировать параметр "минимальная длинна смены"




