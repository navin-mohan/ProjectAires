import modeldb
import gengraph
import getPaths
import networkx as nx

class Store():

	def __init__(self):
		self.title="Call Database"
		modeldb.createtbl()
		self.a=nx.Graph()

	def insert_entry(self,a):
		lat_in=[]
		lon_in=[]
		ano_in=[]
		for i in a:
			lat_in.append(a['lat'])
			lon_in.append(a['lon'])
			ano_in.append(a['ano'])
		for i,j,k in zip(lat_in,lon_in,ano_in):
			self.a=insertdb(i,j,k,a)
			
			
		
