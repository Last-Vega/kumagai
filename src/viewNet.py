import networkx as nx
import numpy as np
import pickle
import matplotlib.pyplot as plt

with open('../vars/createdBy.createdBylist', 'rb') as f:
    createdBy = pickle.load(f)

with open('../vars/c_c.adj', 'rb') as f:
    company_adj = pickle.load(f)

company_adj = company_adj.toarray()
for itr in range(len(company_adj)):
    company_adj[itr, itr] = 0

G = nx.from_numpy_matrix(company_adj)

# nx.draw_networkx(G)
# plt.show()

# # degree_centers = nx.degree_centrality(G)
# # center = sorted(degree_centers.items(), key=lambda x: x[1], reverse=True)[:50]
# # for elm in center:
# #     company_ind = elm[0]
# #     value = elm[1]
# #     print(f'{createdBy[company_ind]}, {value}')
# # print('--------------------------')

eigen_centers = nx.eigenvector_centrality_numpy(G)
eigen = sorted(eigen_centers.items(), key=lambda x: x[1], reverse=True)[:100]

rank = 1
for elm in eigen:
    company_ind = elm[0]
    value = elm[1]
    print(f'{rank}: {createdBy[company_ind]}, {value}')
    rank += 1