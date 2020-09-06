#mydict = {}
#with open('text_5.txt', encoding='utf-8') as f:
    #for line in f:
        #name, stats = line.split(" : ")
        #name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or (i >= '0' and i <= '9')]).split()))
        #mydict[name] = name_sum
    #print(f'{mydict}')

# Никак не пойму, где ошибка, вроде бы в коде ошибки нет, но почему то IndexError.

import re

subs_total_hours = {}

with open('text_5.txt') as f:
    for line in f.readline():
        subs_total_hours[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
    print(subs_total_hours)