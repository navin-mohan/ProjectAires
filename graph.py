import modeldb
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
G.add_node(1,pos=(1,1))
G.add_node(2,pos=(2,2))
G.add_node(3,pos=(1,0))
G.add_node(4,pos=(3,1))
G.add_edge(1,2,weight=0.7017)
G.add_edge(1,3,weight=1)
G.add_edge(1,4,weight=2)
G.add_edge(2,4,weight=0.7017)
G.add_edge(3,4,weight=2.236)


