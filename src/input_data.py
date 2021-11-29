import numpy as np
import networkx as nx
import pickle
from scipy.sparse import csr_matrix, lil_matrix

def make_adj(f_name:str) -> np.ndarray:
    with open(f_name, 'rb') as rb:
        g:any = pickle.load(rb)
    adj:np.ndarray = nx.to_numpy_array(g, dtype=int)
    return adj



f_name:str = '../vars/c_c.graph'
adj:np.ndarray = make_adj(f_name)
adj:csr_matrix = csr_matrix(adj)
print(type(adj))
# print(adj)