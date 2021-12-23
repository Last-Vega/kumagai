import pickle
import json 
# with open('../vars/annotate.ct', 'rb') as rb:
#     annotate_list:list = pickle.load(rb)

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

def makeJson(z_list, centrality_list, data_list, wrd):
    id_dic = {}
    for centrality in centrality_list:
        ind = data_list.index(centrality[0])
        id_dic[ind] = centrality[0]
    
    json_data = []
    for k, v in id_dic.items():
        dic = {}
        z = z_list[k]
        dic[wrd] = v
        dic['x'] = z[0]
        dic['y'] = z[1]
        json_data.append(dic)
    
    result = {'key':json_data}
    return result

def readBinary(f):
    with open(f, 'rb') as bf:
        data = pickle.load(bf)
    return data

f1 = '../vars/createdBy.createdBylist'
f2 = '../vars/term.termlist'
f3 = '../vars/centralityTerm.degree'
f4 = '../vars/centralityCompany.degree'
f5 = '../vars/z_c1221.c'
f6 = '../vars/z_t1221.t'

company_list = readBinary(f1)
term_list = readBinary(f2)
company_centrality = readBinary(f3)
term_centrality = readBinary(f4)
z_c = readBinary(f5)
z_t = readBinary(f6)

company_centrality = company_centrality.items()
company_centrality = list(company_centrality)[:4530]
company_centrality = sorted(company_centrality, key=lambda x: x[1], reverse=True)[:100]


term_centrality = term_centrality.items()
term_centrality = list(term_centrality)[:28093]

term_centrality = sorted(term_centrality, key=lambda x: x[1], reverse=True)[:100]

r1 = makeJson(z_c, company_centrality, company_list, 'company')
r2 = makeJson(z_t, term_centrality, term_list, 'term')

json_file = open('./latentC1223.json', 'w')
json.dump(r1, json_file, indent=2, ensure_ascii=False)
json_file = open('./latentT1223.json', 'w')
json.dump(r2, json_file, indent=2, ensure_ascii=False)

# freq1 = '../data/company_freq.json'
# freq2 = '../data/term_freq.json'
# z1 = '../vars/z.c'
# z2 = '../vars/z.t'

# r1 = createJSON(freq1, z1, annotate_list, 'company')

# json_file = open('./latentC.json', 'w')
# json.dump(r1, json_file, indent=2, ensure_ascii=False)

# term_list = annotate_list[4530:]
# r2 = createJSON(freq2, z2, term_list, 'term')
# json_file = open('./latentT.json', 'w')
# json.dump(r2, json_file, indent=2, ensure_ascii=False)