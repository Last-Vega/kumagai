from networkx.classes.graph import Graph
import numpy as np
import networkx as nx
import pickle
from scipy.sparse import csr_matrix, lil_matrix

def company_adj(f_name:str) -> csr_matrix:
    with open(f_name, 'rb') as rb:
        adj:csr_matrix = pickle.load(rb)
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

f_name:str = '../vars/c_c.adj'
adj:csr_matrix = company_adj(f_name)
# print(adj)
features:lil_matrix = createFeatures(adj)

f_name:str = '../vars/c_t.biadj'
bi_adj:csr_matrix = company_term_biadj(f_name)
# print(bi_adj)