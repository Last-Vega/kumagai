import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix, lil_matrix

n1 = 50
n2 = 80
seed = 42
p = 0.01
g = nx.bipartite.generators.random_graph(n1, n2, p, seed)

# edges = g.edges()
# print(edges)
# exit()

# # nx.draw(g)
# # plt.show()

n1_set = list(range(0, n1))
n2_set = list(range(n1, n1+n2))

edges = g.edges()

B = nx.Graph()
B.add_nodes_from(n1_set, bipartite=0) # Add the node attribute "bipartite"
B.add_nodes_from(n2_set, bipartite=1)

B.add_edges_from(edges)

# Separate by group
# l, r = nx.bipartite.sets(B)
l = set(range(0,n1))
r = set(range(n1, n1+n2))

pos = {}

# Update position for node from each group
pos.update((node, (1, index)) for index, node in enumerate(l))
pos.update((node, (2, index)) for index, node in enumerate(r))

# nx.draw(B, pos=pos)
# plt.show()

bi_networks = np.zeros((n1+n2, n1+n2))

for edge in edges:
    e0 = edge[0]
    e1 = edge[1]
    bi_networks[e0][e1] = 1
    bi_networks[e1][e0] = 1

# print(bi_networks)
bi_networks = csr_matrix(bi_networks)
# print(bi_networks)

# row_order = list(range(0, n1))
# bi_networks = nx.bipartite.matrix.biadjacency_matrix(B, row_order, format='coo')
# print(bi_networks)