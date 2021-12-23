import networkx as nx
import numpy as np
import pickle
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



# with open('../vars/c_t.biadj', 'rb') as f:
#     adj = pickle.load(f)

# adj = adj.toarray()
# G = nx.from_numpy_matrix(adj)
# print(nx.is_bipartite(G))
# print(nx.betweenness_centrality(G))

# bi_centality = nx.betweenness_centrality(G)
# bi_centality = sorted(bi_centality.items(), key=lambda x: x[1], reverse=True)[:50]

# print(bi_centality)

# with open('../vars/c_t.bigraph', 'rb') as f:
#     B = pickle.load(f)
# # print(B)
# bi_centality = nx.betweenness_centrality(B)
# # bi_centality = sorted(bi_centality.items(), key=lambda x: x[1], reverse=True)[:50]

# print(bi_centality)


import networkx as nx
from networkx.algorithms import bipartite

speakers = ['Pink', 'Green']
items = ['Knife', 'Rope']

B = nx.Graph()

B.add_nodes_from(items, bipartite = 0)
B.add_nodes_from(speakers, bipartite = 1)

B.add_edge('Pink', 'Knife', weight = 10)
B.add_edge('Pink', 'Rope', weight = 4)
B.add_edge('Green', 'Rope', weight = 2)
B.add_edge('Green', 'Knife', weight = 7)

bottom_nodes, top_nodes = bipartite.sets(B)
print(bottom_nodes)
print(top_nodes)
print(nx.is_bipartite(B))
print(bipartite.betweenness_centrality(B, bottom_nodes))
print(nx.betweenness_centrality(B))
# print(nx.betweenness_centrality(B, weight = 'weight'))
