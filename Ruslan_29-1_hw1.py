day_1 = int(input('1-day'))
day_2 = int(input('2-day'))
day_2 = int(input('2-day'))
day_3 = int(input('3-day'))
day_4 = int(input('4-day'))
day_5 = int(input('5-day'))
day_6 = int(input('6-day'))
day_7 = int(input('7-day'))


total_amount = day_1 + day_2 + day_3 + day_4 \
    + day_5 + day_6 + day_7
# ПЛЮСУЕМ ВСЕ  ДНИ,
# ПОТОМ ДЕЛИМ ЧТО БЫ УЗНАТЬ СРЕДНИИ РАСХОД В ДЕНЬ

middle = total_amount / 7
print(f'Total amount { total_amount}')
print(round(middle, 1))
# РЕЗУЛЬТАТ  ОКРУГЛЕННЫЙ С ОДНОЙ ЦИФРОЙ ПОСЛЕ ТОЧКИ
# ROUND ИСПОЛЬЗУЕМ ДЛЯ ТОГО,ЧТО БЫ ОКРУГЛИТЬ ЧИСЛО,МЫ УКАЗАЛИ 1, ПОЭТОМУ ОКРУГЛЯТЬСЯ БУДЕТ К 1, БЕЗ  ДАЛЬНЕЙШИХ ЦИФР
