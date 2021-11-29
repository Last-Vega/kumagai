# def create_node(G:any, json_data:dict) -> any:
#     company_list:list = []
#     for itr in range(len(json_data)):
#         itr = str(itr)
#         if 'createdBy' in json_data[itr].keys():
            
#             # data['createdBy'] = re.sub(re_obj, '', data['createdBy'])
#             for company in set(json_data[itr]['createdBy']):
#                 # if not company in company_list:
#                 #     G.add_node(company)
#                 #     company_list.append(company)

#     return G

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
        
        if type(f_term) is str:
            comp_list = re.findall(company_pattern, createdBy)
            json_data[itr]['createdBy'] = comp_list
        
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
            print(itr)
            json_data[itr]['term'] = dic
        
    
    return json_data

import json
import re
import regex
import networkx as nx
import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
import matplotlib.pyplot as plt
import ast

f_name = '../data/patent.json'
json_open = open(f_name, 'r')
json_data = json.load(json_open)

json_data = changeType(json_data)

with open('../data/patent_parsed.json', 'w') as f:
    result = json.dump(json_data, f, indent=2, ensure_ascii=False)


    
# graph:any = nx.Graph()
# G:any = create_node(graph, json_data)
# print(len(G.nodes))
# print(G.nodes)