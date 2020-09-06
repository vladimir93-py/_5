from googletrans import Translator

with open('text_5_translate.txt', 'w', encoding='utf-8') as f:
    with open('homework_5.txt', 'r', encoding='utf-8') as f1:
        text = f1.read()
    f.write(Translator().translate(text, dest='ru').text)

# Никак не пойму, где ошибка, вроде бы в коде ошибки нет, но почему то IndexError.