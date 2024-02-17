import csv
import json
import random

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            writer.writerow(row)

def save_to_json(func):
    def wrapper(*args):
        results = []
        with open(args[0], 'r', encoding='UTF-8') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                roots = func(a, b, c) 
                result = {"parameters": [a, b, c], "result": roots}
                results.append(result)
        with open('results.json', 'w', encoding='UTF-8') as file:
            json.dump(results, file)
    return wrapper

@save_to_json
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2*a)
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2

if __name__ == '__main__':
    generate_csv_file("input_data.csv", 101)

    find_roots("input_data.csv")

    with open("results.json", 'r') as f:
        data = json.load(f)

    if 100<=len(data)<=1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

    print(len(data)==101)