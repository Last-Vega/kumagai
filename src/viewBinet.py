import networkx as nx
import numpy as np
import pickle
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite

with open('../vars/centralityTerm.degree', 'rb') as f1:
    company_centrality = pickle.load(f1)

with open('../vars/centralityCompany.degree', 'rb') as f2:
    term_centrality = pickle.load(f2)

company_centrality = company_centrality.items()
company_centrality = list(company_centrality)[:4530]
company_centrality = sorted(company_centrality, key=lambda x: x[1], reverse=True)[:100]
print(company_centrality)

term_centrality = term_centrality.items()
term_centrality = list(term_centrality)[:28093]

term_centrality = sorted(term_centrality, key=lambda x: x[1], reverse=True)[:100]
print(term_centrality)

