import json
import re

f_name:str = '../data/patent_parsed0119_1.json'
json_open = open(f_name, 'r')
json_data:dict = json.load(json_open)

for itr in range(len(json_data)):
    re_obj = '^.{4}'
    i = str(itr)
    # if 'term' in json_data[i]:
    #     dc = {k: v for k, v in json_data[i]['term'].items() if v > 5}
    #     # print(dc)
    #     json_data[i]['term'] = dc
    if 'all_dic' in json_data[i]:
        dc = {k: v for k, v in json_data[i]['all_dic'].items() if v > 2}
        # print(dc)
        json_data[i]['term'] = dc
    
    if 'headIPC' in json_data[i]:
        headIPC = re.findall(re_obj, json_data[i]['headIPC'])[0]
        json_data[i]['headIPC'] = headIPC

    if 'createdAt' in json_data[i]:
        createdAt = re.findall(re_obj, json_data[i]['createdAt'])[0]
        json_data[i]['createdAt'] = createdAt
        
    

with open('../data/patent0119_1.json', 'w') as f:
    result = json.dump(json_data, f, indent=2, ensure_ascii=False)