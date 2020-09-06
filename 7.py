import _json

result = []
with open('test_7.json', 'w', encoding='utf-8') as f:
    with open('text_5.txt', encoding='utf-8')as f_1:
        profit = {}
        for line in f_1:
            profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        average_profit = sum([int(i) for i in profit.values() if int(i) > 0]) / len(
            [int(i) for i in profit.values() if int(i) > 0])
        result.append(profit)
        result.append({'average_profit': round(average_profit)})
    _json.dump(result, f)
        #где-то я ошибся (((