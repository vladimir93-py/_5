with open("homework_5.txt", "r", encoding="utf-8") as my_file:
    s_sum = []
    less = []
    line = my_file.read().split("\n")
    for i in line:
        i = i.split()
        if float(i[1]) > 20000: # Ошибка ValueError. подскажите в чем ошибка.
            less.append(i[0])
        s_sum.append(i[1])

print(f"Salary less 20 000 {less}. Average salary - {sum(map(float, s_sum)) / len(s_sum)}")
