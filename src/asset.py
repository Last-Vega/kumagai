import pickle
import json 
with open('../vars/annotate.ct', 'rb') as rb:
    annotate_list:list = pickle.load(rb)

f1 = '../data/company_freq.json'
f2 = '../data/term_freq.json'
with open(f2, 'r') as j1:
    cf = json.load(j1)

d = {}
for k,v in cf.items():
    if v > 100:
        d[k] = v
    else:
        break
id_dic = {}
for k in d.keys():
    ind = annotate_list.index(k)
    id_dic[ind] = k

