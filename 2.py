counter = 0
with open('homework_5.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        counter += 1
        line_words = line.split()
        print(line, 'Количество строк: ', len(line_words))
    print('Количество всех строк: ', counter)
    