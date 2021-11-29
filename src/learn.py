import torch
import torch.nn.functional as F
from args import *
import os
from util import fix_seed, prepare_adj_for_training, prepare_features_for_training, model_init

from input_data import adj, features, bi_adj

fix_seed(42)
# Train on CPU (hide GPU) due to memory constraints
os.environ['CUDA_VISIBLE_DEVICES'] = ""

weight_tensor, adj_norm, norm, adj_label, adj_orig, test_edges, test_edges_false = prepare_adj_for_training(adj)
features = prepare_features_for_training(features)
graph_dim = features.shape[1]

bi_weight_tensor, bi_adj_norm, bi_norm, bi_adj_label, bi_adj_orig, bi_test_edges, bi_test_edges_false = prepare_adj_for_training(bi_adj)
bipartite_dim = bi_adj.shape[1]


model, optimizer = model_init(adj_norm, graph_dim, bipartite_dim)

for epoch in range(num_epoch):
    A_pred, Bi_pred = model(features, bi_adj_norm)
    optimizer.zero_grad()
    loss = norm*F.binary_cross_entropy(A_pred.view(-1), adj_label.to_dense().view(-1), weight = weight_tensor) + bi_norm*F.binary_cross_entropy(Bi_pred.view(-1), bi_adj_label.to_dense().view(-1), weight = bi_weight_tensor)
    kl_divergence1 = 0.5/ A_pred.size(0) * (1 + 2*model.logstd - model.mean**2 - torch.exp(model.logstd)**2).sum(1).mean()
    kl_divergence2 = 0.5/ Bi_pred.size(0) * (1 + 2*model.siguma - model.mu**2 - model.siguma**2).sum(1).mean()
    loss -= kl_divergence1
    loss -= kl_divergence2
    loss.backward()
    optimizer.step()
    print(loss)


# Latent variable of Company graph
Z_c = model.Z_c.to('cpu').detach().numpy().copy().tolist()

# Latent variable of Company-Patent Bipartite graph
Z_p = model.Z_p.to('cpu').detach().numpy().copy().tolist()
Z_p = Z_p[num_company:]

zc_x = [d[0] for d in Z_c]
zc_y = [d[1] for d in Z_c]

zp_x = [d[0] for d in Z_p]
zp_y = [d[1] for d in Z_p]
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8.0, 6.0))

sc = ax.scatter(zc_x, zc_y, label='Company', color='red')
sc2 = ax.scatter(zp_x, zp_y, label='Term', color='blue')

ax.legend(loc=0)

plt.show()