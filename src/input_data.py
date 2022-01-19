from networkx.classes.graph import Graph
import numpy as np
import networkx as nx
import pickle
from scipy.sparse import csr_matrix, lil_matrix

def loadBinary(f_name:str) -> csr_matrix:
    with open(f_name, 'rb') as rb:
        adj:csr_matrix = pickle.load(rb)
    return adj

def createFeatures(adj:csr_matrix) -> lil_matrix:
    n = adj.shape[0]

    features = np.zeros((n, n))
    for i in range(n):
        features[i][i] = 1
    features = lil_matrix(features)
    return features

f_name = f'../vars/W_adj.adj'
adj:csr_matrix = loadBinary(f_name)

features:lil_matrix = createFeatures(adj)

f_name:str = f'../vars/W_bi.adj'
bi_adj:csr_matrix = loadBinary(f_name)

# f_name:str = '../vars/c_c.adj'
# adj:csr_matrix = loadBinary(f_name)

# features:lil_matrix = createFeatures(adj)

# f_name:str = '../vars/c_t.biadj'
# bi_adj:csr_matrix = loadBinary(f_name)

# with open('../vars/annotate.ct', 'rb') as rb:
#     annotate_list:list = pickle.load(rb)
