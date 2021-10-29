import torch
import torch.nn.functional as F
from args import *
import os
from util import prepare_adj_for_training, prepare_features_for_training, model_init

from sample_graph import adj, features

# Train on CPU (hide GPU) due to memory constraints
os.environ['CUDA_VISIBLE_DEVICES'] = ""

weight_tensor, adj_norm, norm, adj_label, adj_orig, test_edges, test_edges_false = prepare_adj_for_training(adj)

features = prepare_features_for_training(features)

input_dim = features.shape[1]

model, optimizer = model_init(adj_norm, input_dim)

for epoch in range(num_epoch):
    A_pred = model(features)
    optimizer.zero_grad()
    loss = log_lik = norm*F.binary_cross_entropy(A_pred.view(-1), adj_label.to_dense().view(-1), weight = weight_tensor)
    
    loss.backward()
    optimizer.step()

print(A_pred[3])