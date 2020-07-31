import os
import csv
import re
import requests


# format the csv
output_directory = 'images/'
csv_filepath = 'images.csv'

input_file = csv.DictReader(open(csv_filepath, encoding='utf-8'))

output_dict = {}

for row in input_file:
    # print(row["Internal ID"])
    output_list = []
    for col in row:

        if row[col]:
            output_list.append(row[col])
    output_dict.update({output_list[:1][0]: output_list[1:]})

# os.makedirs(os.path.dirname(output_directory), exist_ok=True)

for item in output_dict:
    
    for url in output_dict[item]:
        print(item, url)
        regex = re.search('https://images.zentail.com/1077/(.*)', url, re.IGNORECASE)
        if regex:
            output_file = f'images/{item}/{regex.group(1)}'
            r = requests.get(url, stream=True)
            if r.status_code == 200:
                os.makedirs(os.path.dirname(output_file), exist_ok=True)
                with open(output_file, 'wb') as f:
                    f.write(r.content)
