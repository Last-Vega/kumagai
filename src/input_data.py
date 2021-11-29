from networkx.classes.graph import Graph
import numpy as np
import networkx as nx
import pickle
from scipy.sparse import csr_matrix, lil_matrix

def company_adj(f_name:str) -> csr_matrix:
    with open(f_name, 'rb') as rb:
        g:Graph = pickle.load(rb)
    adj:np.ndarray = nx.to_numpy_array(g, dtype=int)
    adj:csr_matrix = csr_matrix(adj)
    return adj

def company_term_biadj(f_name:str) -> csr_matrix:
    with open(f_name, 'rb') as rb:
        bi_adj:csr_matrix = pickle.load(rb)
    return bi_adj

def createFeatures(adj:csr_matrix) -> lil_matrix:
    n = adj.shape[0]

    features = np.zeros((n, n))
    for i in range(n):
        features[i][i] = 1
    features = lil_matrix(features)
    return features

f_name:str = '../vars/c_c.graph'
adj:csr_matrix = company_adj(f_name)

features:lil_matrix = createFeatures(adj)

f_name:str = '../vars/c_t.biadj'
bi_adj:csr_matrix = company_term_biadj(f_name)
