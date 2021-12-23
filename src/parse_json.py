def changeType(json_data:dict) -> dict:
    company_pattern = r"((?:[^\\']+|\\.){3})"
    term_pattern = r"[a-z]"
    for itr in range(len(json_data)):
        itr = str(itr)
        f_term = json_data[itr]['f_term']
        createdBy = json_data[itr]['createdBy']
        term = json_data[itr]['term']
        if type(f_term) is str:
            json_data[itr]['f_term'] = f_term.split(',')
        else:
            json_data[itr]['f_term'] = ['']
        
        if type(createdBy) is str:
            comp_list = re.findall(company_pattern, createdBy)
            json_data[itr]['createdBy'] = comp_list
        # else:
        #     print(json_data[itr]['createdBy'])
        #     print(type(json_data[itr]['createdBy']))
        
        if type(term) is str:
            if regex.search(term_pattern, term):
                term = term.lstrip('{')
                term = term.rstrip('}')
                term = term.split(',')
                for i in range(len(term)):
                    if regex.search(term_pattern, term[i]):
                        term[i] = ''
                term = [s for s in term if s != '']
                term = ','.join(term)

                p = r'\s'
                term = re.sub(p, '', term)
                term = "{"+term+"}"
                dic = ast.literal_eval(term)
            else:
                dic = ast.literal_eval(term)
            json_data[itr]['term'] = dic
        
    
    return json_data

import json
import re
import regex
import ast

f_name = '../data/patent1217.json'
json_open = open(f_name, 'r')
json_data = json.load(json_open)

json_data = changeType(json_data)

with open('../data/patent_parsed1217.json', 'w') as f:
    result = json.dump(json_data, f, indent=2, ensure_ascii=False)

