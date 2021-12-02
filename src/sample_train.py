import numpy as np
from args import *
import matplotlib.pyplot as plt
import json

from asset import id_dic
fig, ax = plt.subplots(figsize=(8.0, 6.0))
# Z = np.random.rand(num_patent,2)
Z = np.random.normal(0, 0.1, size=(num_patent, 2))
Z_c = Z[:num_company]
Z_t = Z[num_company:]

js = []

for k, v in id_dic.items():
    dic = {}
    z = Z_t[k].tolist()
    dic['term'] = v
    dic['x'] = z[0]
    dic['y'] = z[1]
    js.append(dic)

result = {'key':js}
json_file = open('./latentT.json', 'w')
json.dump(result, json_file, indent=2, ensure_ascii=False)

# zc_x = [d[0] for d in Z_c]
# zc_y = [d[1] for d in Z_c]
# sc = ax.scatter(zc_x, zc_y, label='Company', color='red')

# zt_x = [d[0] for d in Z_t]
# zt_y = [d[1] for d in Z_t]

# sc2 = ax.scatter(zt_x, zt_y, label='Term', color='blue')
# ax.legend(loc=0)

# plt.show()