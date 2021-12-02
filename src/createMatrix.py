import json
import numpy as np
from args import num_company, num_patent, num_term
from scipy.sparse import csr_matrix, lil_matrix


def createRelationList(json_data:dict, relation:str) -> list:
    relation_list:list = []
    for itr in range(len(json_data)):
        itr = str(itr)
        for c in json_data[itr][relation]:
            if c not in relation_list:
                relation_list.append(c)
    
    return relation_list

def createMtr(matrix:np.ndarray, relation:str, relation_list:list, json_data:dict) -> np.ndarray:
    for itr in range(num_patent):
        i = str(itr)
        for c in json_data[i][relation]:
            ind:int = relation_list.index(c)
            matrix[itr][ind] = 1 
    return matrix

def createMetaBaseAdj(m1:np.ndarray, m2:np.ndarray) -> np.ndarray:
    # 2つのpatent-***の関係を，行列の積を用いることで，***-***にする
    meta_base_matrix:np.ndarray = np.matmul(m1.T, m2)

    # 対角成分を0にする
    for itr in range(len(meta_base_matrix)):
        meta_base_matrix[itr][itr] = 0
    
    return meta_base_matrix


with open('../data/patent_parsed.json', 'r') as f:
    json_data = json.load(f)

company_list = createRelationList(json_data, 'createdBy')
term_list = createRelationList(json_data, 'term')

# # 行列の初期化
# P_C_Matrix:np.ndarray = np.zeros((num_patent, num_company))
# P_T_Matrix:np.ndarray = np.zeros((num_patent, num_term))


# # company-company 隣接行列
# P_C_Matrix = createMtr(P_C_Matrix, 'createdBy', company_list, json_data)
# c_c_adj = createMetaBaseAdj(P_C_Matrix, P_C_Matrix)
# c_c_adj = csr_matrix(c_c_adj)

# # company-term二部グラフ隣接行列
# P_T_Matrix = createMtr(P_T_Matrix, 'term', term_list, json_data)
# bi_adj = createMetaBaseAdj(P_C_Matrix, P_T_Matrix)
# bi_adj = csr_matrix(bi_adj)
# print(bi_adj)