def create_node(G:any, json_data:dict) -> any:
    company_list:list = []
    for itr in range(len(json_data)):
        itr = str(itr)
        if 'createdBy' in json_data[itr].keys():
 
            for company in json_data[itr]['createdBy']:
                if not company in company_list:
                    G.add_node(company)
                    company_list.append(company)

    return G

import json
import re
import regex
import networkx as nx
import numpy as np
from scipy.sparse import csr_matrix, lil_matrix

f_name = '../data/patent_parsed.json'
json_open = open(f_name, 'r')
json_data = json.load(json_open)
    
graph:any = nx.Graph()
G:any = create_node(graph, json_data)

print(len(G.nodes()))
# print(G.nodes())