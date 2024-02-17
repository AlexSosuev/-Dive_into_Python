# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел. Напишите функцию, которая создаёт 
# из созданного ранее файла новый с данными в формате JSON. Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

import json

def convert_to_json(input_file, output_fil):
    data = {}
    with open(input_file, 'r') as file:
        for line in file:
            name, number = line.strip().split(' | ')
            data[name.strip().capitalize()] = float(number)
    with open(output_fil, w, encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

convert_to_json('result.txt', 'result.json')