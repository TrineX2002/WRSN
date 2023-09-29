import csv
import numpy as np
import yaml
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

with open('hanoi1000n200g.csv', 'r') as file:
    data_csv = csv.reader(file)
    for row in data_csv:
        target_a = row[1]
        node_a =row[2]
with open('hanoi1000n100g.csv', 'r') as file:
    data_csv = csv.reader(file)
    for row in data_csv:
        target_b = row[1]
        node_b =row[2]
target = np.array([tuple(map(float, pair.strip("()").replace("(", "").replace(")", "").replace(" ", "").split(","))) for pair in target_b.split(",")])
node = np.array([tuple(map(float, pair.strip("()").replace("(", "").replace(")", "").replace(" ", "").split(","))) for pair in node_a.split(",")])
node = node.reshape(-1, 2)
target = target.reshape(-1, 2)
x = [point[0] for point in node]
y = [point[1] for point in node]
plt.scatter(x,y,c='b')
a = [point[0] for point in target]
b = [point[1] for point in target]
plt.scatter(a,b,c='r')
for i in range(len(node)):
    circle = Circle((x[i], y[i]), 80, edgecolor='blue', facecolor='none')
    plt.gca().add_patch(circle)

plt.show()