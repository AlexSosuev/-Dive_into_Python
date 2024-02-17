# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import json, csv

def json_to_csv(filename: str):
    with open(filename, 'r', encoding = 'utf-8') as file:
        json_dict = json.load(file)
    user_list = []
    for u_lvl, user in json_dict.items():
        for u_id, u_name in user.items():
            user_list.append((u_name, u_id, u_lvl))    
    with open(filename.split('.')[0] + '.csv', 'w', encoding='utf-8') as csv_file:
        csv_write = csv.writer(csv_file, delimeter=';', linetermonator='\n')
        csv_write.writerow(['name', 'ID','Level'])
        csv_write.writerow(user_list) 

json_to_csv('workers.json')