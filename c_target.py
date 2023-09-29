import yaml
import numpy as np

with open('hanoi1000n50.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
target=np.array(data['targets'])
node=np.array(data['nodes'])
print(len(target))
print(len(node))
# min=999999
# id=0
# target_new=np.zeros(len(target))
# for i in range(len(target)):
#     for j in range(len(node)):
#         kc=np.linalg.norm(target[i]-node[j])
#         if (min>kc): 
#             min=kc
#             id=j
#     target_new[i]=id
#     min=999999
# def remove_duplicates(target_new):
#     unique_items = []
#     for item in target_new:
#         if item not in unique_items:
#             unique_items.append(item)
#     return unique_items
# result = remove_duplicates(target_new)
# print(result)