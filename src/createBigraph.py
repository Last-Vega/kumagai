import json
import networkx as nx
from networkx.algorithms import bipartite
from networkx.classes.graph import Graph
import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
import pickle

def create_Company_node(G:Graph, json_data:dict) -> Graph:
    company_list:list = []
    for itr in range(len(json_data)):
        itr = str(itr)
        if 'createdBy' in json_data[itr].keys():
            for company in json_data[itr]['createdBy']:
                if not company in company_list:
                    G.add_node(company)
                    company_list.append(company)

    return G

def create_Term_node(G:Graph, json_data:dict) -> Graph:
    term_list:list = []
    for itr in range(len(json_data)):
        itr = str(itr)
        if 'term' in json_data[itr].keys():
            for term in json_data[itr]['term']:
                if not term in term_list:
                    G.add_node(term)
                    term_list.append(term)

    return G

def makeBirelation(patent_info:dict, json_data:dict, G:Graph, itr:str) -> None:
    for company in patent_info['createdBy']:
        for term in patent_info['term']:
            print(itr)
            for i in range(len(json_data)):
                if int(itr) > i:
                    continue
                else:
                    i = str(i)
                    if 'term' in json_data[i].keys():
                        term_list = json_data[i]['term']
                        for comp_term in term_list:
                            if comp_term == term:
                                G.add_edge(company, comp_term)
    return None

def buildBigraph(G:Graph, json_data:dict) -> Graph:
    for itr in range(len(json_data)):
        itr = str(itr)
        if 'createdBy' in json_data[itr].keys() and 'term' in json_data[itr].keys():
            makeBirelation(json_data[itr], json_data, G, itr)
    return G

f_name:str = '../data/patent_parsed.json'
# f_name:str = '../data/sample.json'


json_open = open(f_name, 'r')
json_data:dict = json.load(json_open)

graph:Graph = nx.Graph()
G1:Graph = create_Company_node(graph, json_data)
G2:Graph = create_Term_node(graph, json_data)

B:Graph = nx.Graph()
B.add_nodes_from(G1.nodes(), bipartite=0)
B.add_nodes_from(G2.nodes(), bipartite=1)
B = buildBigraph(B, json_data)
bi_adj:csr_matrix = bipartite.matrix.biadjacency_matrix(B, G1.nodes(), G2.nodes())

with open('../vars/c_t.bigraph', 'wb') as bf:
    pickle.dump(B, bf)

with open('../vars/c_t.biadj', 'wb') as bf2:
    pickle.dump(bi_adj, bf2)

# print(bi_adj)
# print(B.edges())
# print(B.nodes())
# print(len(G.nodes()))