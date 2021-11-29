import pickle
import numpy as np
with open('../vars/c_cAdj.adj', 'rb') as rb:
    adj = pickle.load(rb)

print(adj)
print(len(adj))
