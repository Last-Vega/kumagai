import json
from typing_extensions import Literal
import networkx as nx
from networkx.classes.graph import Graph
import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
import itertools

def create_node(G:any, json_data:dict) -> Graph:
    term_list:list = []
    for itr in range(len(json_data)):
        itr = str(itr)
        if 'term' in json_data[itr].keys():
            for term in json_data[itr]['term']:
                if not term in term_list:
                    G.add_node(term)
                    term_list.append(term)

    return G

f_name:str = '../data/patent_parsed.json'

json_open = open(f_name, 'r')
json_data:dict = json.load(json_open)

graph:Graph = nx.Graph()
G:Graph = create_node(graph, json_data)

print(G.nodes())
print(len(G.nodes()))