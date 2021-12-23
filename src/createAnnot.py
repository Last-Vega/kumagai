import pickle

f1 = '../vars/createdBy.createdBylist'
f2 = '../vars/term.termlist'

with open(f1, 'rb') as l1:
    createdBy = pickle.load(l1)

with open(f2, 'rb') as l2:
    term = pickle.load(l2)

print(term[0])
# annotate_list = createdBy + term
# print(len(annotate_list))
# print(annotate_list[4530:])
# print(createdBy[:20])
# print(term[:20])