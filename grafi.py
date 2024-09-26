import networkx as nx
import random
import matplotlib.pyplot as plt

graph = nx.Graph()
a = ['A', 'B', 'C', 'D', 'E', 'F'][:random.randint(2, 6)]
for i in a:
    graph.add_node(i)
for i in range(len(a) * 2):
    b = random.choice(a)
    c = random.choice(a)
    if b != c:
        graph.add_edge(b, c, weight=random.randint(1, 20))
pos = nx.circular_layout(graph)
nx.draw(graph, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_weight)
plt.show()
