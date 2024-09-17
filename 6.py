with open('file.txt', 'w') as file:
    file.write('Hello World!\n')

with open('file.txt', 'r') as file:
    content = file.read()
    print(content)

import json

data = {
    'ism': 'Azizbek',
    'yosh': 18,
    'shahar': 'Toshkent'
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

with open('data.json', 'r') as json_file:
    data_loaded = json.load(json_file)
    print(data_loaded)