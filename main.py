import pandas as pd
from numpy import genfromtxt
import matplotlib.pyplot as plt
import networkx as nx


mydata = genfromtxt('file.txt', delimiter=' ')
G = nx.DiGraph(mydata)

print(G)
print(len(G.nodes), len(G.edges))

if len(G.edges) > (len(G.nodes)-1)*(len(G.nodes)-2)*0.5:
    print("related graph")
else:
    print("unrelated graph")
    
nx.draw(G, with_labels=True)
plt.show()
