import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.parameter import Parameter
import os
import numpy as np
import args

class VGAE(nn.Module):
	def __init__(self, adj, input_dims):
		super(VGAE,self).__init__()
		self.base_gcn = GraphConvSparse(input_dims, args.hidden1_dim, adj)
		self.gcn_mean = GraphConvSparse(args.hidden1_dim, args.hidden2_dim, adj, activation=lambda x:x)
		self.gcn_logstddev = GraphConvSparse(args.hidden1_dim, args.hidden2_dim, adj, activation=lambda x:x)

	def encode(self, X):
		hidden = self.base_gcn(X)
		self.mean = self.gcn_mean(hidden)
		self.logstd = self.gcn_logstddev(hidden)
		gaussian_noise = torch.randn(X.size(0), args.hidden2_dim)
		sampled_z = gaussian_noise*torch.exp(self.logstd) + self.mean
		# sampled_z = self.mean
		self.z = sampled_z
		return sampled_z

	def forward(self, X):
		Z = self.encode(X)
		A_pred = norm_distance_decode(Z)
		return A_pred

class GraphConvSparse(nn.Module):
	def __init__(self, input_dim, output_dim, adj, activation = F.relu, **kwargs):
		super(GraphConvSparse, self).__init__(**kwargs)
		self.weight = glorot_init(input_dim, output_dim) 
		self.adj = adj
		self.activation = activation
		# self.dropout = nn.Dropout(0.5)

	def forward(self, inputs):
		x = inputs
		x = torch.mm(x,self.weight)
		x = torch.mm(self.adj, x)
		# x = self.dropout(x)
		outputs = self.activation(x)
		# return outputs
		return x


def norm_distance_decode(Z, a, b):
	import sys
	eps = 0.00001
	z_dist = torch.cdist(Z, Z, p=2) # norm distance
	x = 1/(z_dist + eps)
	A_pred = torch.sigmoid((x/a)-b)

	return A_pred

def glorot_init(input_dim, output_dim):
	init_range = np.sqrt(6.0/(input_dim + output_dim))
	initial = torch.rand(input_dim, output_dim)*2*init_range - init_range
	return nn.Parameter(initial)


class GAE(nn.Module):
	def __init__(self,adj, input_dims):
		super(GAE,self).__init__()
		self.base_gcn = GraphConvSparse(input_dims, args.hidden1_dim, adj)
		self.gcn_mean = GraphConvSparse(args.hidden1_dim, args.hidden2_dim, adj, activation=lambda x:x)
		self.a = Parameter(torch.FloatTensor(1))
		self.b = Parameter(torch.FloatTensor(1))
		nn.init.constant_(self.a, 3)
		nn.init.constant_(self.b, 5)

	def encode(self, X):
		hidden = self.base_gcn(X)
		z = self.mean = self.gcn_mean(hidden)
		self.z = z
		return z

	def forward(self, X):
		Z = self.encode(X)
		A_pred = norm_distance_decode(Z, self.a, self.b)
		return A_pred


class Bipartite_GAE(nn.Module):
	def __init__(self, input_dims):
		super(Bipartite_GAE,self).__init__()
		self.l1 = torch.nn.Linear(input_dims, args.hidden1_dim)
		self.l2 = torch.nn.Linear(args.hidden1_dim, args.hidden2_dim)
		self.weight = glorot_init(args.hidden1_dim, args.hidden2_dim)

	
	def encoder_with_MLP(self, bi_networks):
		h1 = self.l1(bi_networks)
		h2 = torch.sigmoid(h1)
		h3 = self.l2(h2)
		mu = F.relu(self.weight*h3)
		z = mu
		self.z = z
		return z

	def forward(self, bi_networks):
		Z = self.encoder_with_MLP(bi_networks)
		bi_network_pred = norm_distance_decode(Z, a, b)
		return bi_network_pred