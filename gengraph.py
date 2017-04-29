import networkx as nx
import numpy as np 
import haver_sine
	
def add_node(graph,id_node):
	graph.add_node(id_node,pos=(id_node,id_node))
	return graph
	
def add_edge(graph,id_one,id_two,weight):
	graph.add_edge(id_one,id_two,weight=weight)
	return graph

def find_neighbour(list_sql,graph,count):
	lat=[x[1] for x in list_sql]
	lon=[y[2] for y in list_sql]
	for i in range(1,count-1):
		dist=haver_sine.calc_dist(lat[i],lat[count-1],lon[i],lon[count-1])
		if(dist<100):
			graph=add_edge(graph,i,count-1,dist)
	return graph	
