import json
import networkx as nx
import numpy as np
import itertools
from networkx.classes.graph import Graph

def create_node(G:Graph, json_data:dict) -> Graph:
    company_list:list = []
    for itr in range(len(json_data)):
        itr = str(itr)
        if 'createdBy' in json_data[itr].keys():
            for company in json_data[itr]['createdBy']:
                if not company in company_list:
                    G.add_node(company)
                    company_list.append(company)

    return G

def makeCompanyRelation(patent_info:dict, json_data:dict, G:Graph, itr:str) -> None:
    if len(patent_info['createdBy']) > 1:
        comb = list(itertools.combinations(patent_info['createdBy'], 2))
        for elm in comb:
            G.add_edge(elm[0], elm[1])

    for company in patent_info['createdBy']:
        print(itr)
        for i in range(len(json_data)):
            if int(itr) >= i:
                continue
            else:
                i = str(i)
                if 'createdBy' in json_data[i].keys():
                    comp_company_list = json_data[i]['createdBy']
                    for comp_company in comp_company_list:
                        if comp_company == company:
                            G.add_edge(company, comp_company)
    return 

def buildCompanyGraph(G:Graph, json_data:dict) -> Graph:
    for itr in range(len(json_data)):
        itr = str(itr)
        if 'createdBy' in json_data[itr].keys():
            makeCompanyRelation(json_data[itr], json_data, G, itr)
    return G



# f_name = '../data/sample.json'
f_name = '../data/patent_parsed.json'

json_open = open(f_name, 'r')
json_data = json.load(json_open)
    
graph:Graph = nx.Graph()
G:Graph = create_node(graph, json_data)
G = buildCompanyGraph(G, json_data)
adj:np.ndarray = nx.to_numpy_array(G, dtype=int)
print(adj)


import pickle
with open('../vars/c_c.graph', 'wb') as bf:
    pickle.dump(G, bf)

with open('../vars/c_cAdj.adj', 'wb') as bf2:
    pickle.dump(adj, bf2)
