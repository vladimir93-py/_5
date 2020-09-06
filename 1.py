with open('homework_5.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Напишите любые слова в строку или оставьте строку пустой для завершения:\n ')
        if not line:
            break

        print(line, file=f)

