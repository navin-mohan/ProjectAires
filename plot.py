import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(G):	
	pos=nx.get_node_attributes(G,'pos')
	nx.draw(G,pos)
	labels = nx.get_edge_attributes(G,'weight')
	nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
	plt.savefig('test.png')

