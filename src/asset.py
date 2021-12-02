import pickle
import json 
with open('../vars/annotate.ct', 'rb') as rb:
    annotate_list:list = pickle.load(rb)

def createJSON(f1, f2, annotate_list, wrd):
    with open(f1, 'r') as j1:
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
    
    with open(f2, 'rb') as j2:
        Z = pickle.load(j2)

    js = []
    for k, v in id_dic.items():
        dic = {}
        z = Z[k]
        dic[wrd] = v
        dic['x'] = z[0]
        dic['y'] = z[1]
        js.append(dic)

    result = {'key':js}
    return result



freq1 = '../data/company_freq.json'
freq2 = '../data/term_freq.json'
z1 = '../vars/z.c'
z2 = '../vars/z.t'

r1 = createJSON(freq1, z1, annotate_list, 'company')

json_file = open('./latentC.json', 'w')
json.dump(r1, json_file, indent=2, ensure_ascii=False)

term_list = annotate_list[4530:]
r2 = createJSON(freq2, z2, term_list, 'term')
json_file = open('./latentT.json', 'w')
json.dump(r2, json_file, indent=2, ensure_ascii=False)