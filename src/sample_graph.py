import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
#ノードの数
n = 50

#辺ができる確率
p = 0.05

#乱数のシード値
seed = 42

g = nx.random_graphs.fast_gnp_random_graph(n, p, seed, directed=False)

adj = np.zeros((n,n))
edges = g.edges()

for edge in edges:
    e0 = edge[0]
    e1 = edge[1]
    adj[e0][e1] = 1
    adj[e1][e0] = 1

adj = csr_matrix(adj)

features = np.zeros((50, 50))
count = 0
for elm in features:
    elm[count] += 1
    count += 1

features = lil_matrix(features)




