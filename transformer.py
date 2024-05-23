import pandas as pd
import json
import re
import os


def find(name, path):
    cnt = 0
    for root, dirs, files in os.walk(path):
        if name in files:
            cnt = 1
    return cnt


number_of_files = 0
while find(f'intermediate_data{number_of_files + 1}.json', os.getcwd()) != 0:
    number_of_files += 1

df = None
for number in range(1, number_of_files + 1):
    with open(f'intermediate_data{number}.json', 'r', encoding='utf-8') as f_in:
        data = json.load(f_in)
        number_of_flats = len(data)

    list_for_df = []
    for number in range(1, number_of_flats + 1):
        number = str(number)
        flat = data[number]
        features = flat[0]

        region = 'Новосибирская область'
        city = 'Новосибирск'
        district = None
        street = None
        house = None
        metro = None
        rooms = None
        square = None
        floor = None
        number_of_floors = None
        price = flat[1]
        description = flat[2]
        link = flat[3]

        for index, string in enumerate(features):
            if 'р-н' in string:
                district = features[index]

            if 'улица' in string:
                street = features[index]

            pattern1 = r'^(\d{1,3})/(\d{1,3})$'
            pattern2 = r'^(\d{1,3})([A-Za-zА-Яа-я]{1})(\d{1,2})?$'
            if string.isdigit() or bool(re.match(pattern1, string)) or bool(re.match(pattern2, string)):
                house = features[index]

            if 'м.' in string:
                metro = features[index]

            if ',' in string and (string[0].isdigit() or string[0] == 'С'):
                title = features[index]
                first_virgule_index = title.find(',')
                last_virgule_index = title.rfind(',')
                slash_index = title.rfind('/')
                rooms = title[0:first_virgule_index]
                square = title[first_virgule_index + 1:last_virgule_index].strip()
                floor = title[last_virgule_index + 2:slash_index]
                number_of_floors = title[slash_index + 1:slash_index + 3].strip()

        if district is None:
            for index, string in enumerate(features):
                if 'Затулинский жилмассив' in string:
                    district = 'р-н Кировский'

        if street is None:
            for index, string in enumerate(features):
                if 'проспект' in string or 'бульвар' in string or 'переулок' in string:
                    street = features[index]
            if street is None:
                for index, string in enumerate(features):
                    if 'мкр.' in string:
                        street = features[index]

        structured_data = [region, city, district, street, house, metro, price, rooms, square, floor, number_of_floors,
                           link, description]

        list_for_df.append(structured_data)

    if df is None:
        df = pd.DataFrame(list_for_df, columns=['region', 'city', 'district', 'street', 'house', 'metro', 'price',
                                                'rooms', 'square', 'floor', 'number_of_floors', 'link', 'description'])
    else:
        new_df = pd.DataFrame(list_for_df, columns=['region', 'city', 'district', 'street', 'house', 'metro', 'price',
                                                    'rooms', 'square', 'floor', 'number_of_floors', 'link',
                                                    'description'])
        df = pd.concat([df, new_df])

with pd.ExcelWriter('таблица.xlsx') as writer:
    df.to_excel(writer, sheet_name='Данные', index=False)
