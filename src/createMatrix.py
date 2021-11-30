import json
import numpy as np
from args import num_company, num_patent, num_term
with open('../data/patent_parsed.json', 'r') as f:
    json_data = json.load(f)

company_list:list = []
for itr in range(len(json_data)):
    itr = str(itr)
    for c in json_data[itr]['createdBy']:
        if c not in company_list:
            company_list.append(c)


P_C_Matrix = np.zeros(num_patent, num_company)
P_T_Matrix = np.zeros(num_patent, num_term)