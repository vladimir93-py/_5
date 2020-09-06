from random import randint

sum_el = 0
with open('text_5.txt', 'w', encoding='utf-8') as my_file:
    for i in range(100):
        el = randint(1, 100)
        sum_el += el
        my_file.write(str(el) + " ")

    print(f'Сумма элементов - {sum_el}')