import sqlite3 as sql
import gengraph
import networkx as nx
import plot
import getPaths

count=0


def createtbl():
	con=sql.connect('database.db')
	cur=con.cursor()
	cur.execute("CREATE TABLE if not exists users( id integer primary key autoincrement,latitude float not null,longitude float not null,anomaly float not null)");

def filterdata():
	con=sql.connect('database.db')
	cur=con.cursor()
	cur.execute("DELETE FROM users WHERE date < (CURDATE() - INTERVAL 1 DAY)");
	con.commit()
	con.close()

def insert_db(latitude_in,longitude_in,anomaly,g):
	con=sql.connect('database.db')
	cur=con.cursor()
	cur.execute("INSERT INTO users(latitude,longitude,anomaly) VALUES(?,?,?)",(latitude_in,longitude_in,anomaly))
	global count
	count=count+1
	con.commit()
	cur_data=get_data()
	x=[y[0] for y in cur_data] 
	g=gengraph.add_node(g,x[count-1],anomaly)
	g=gengraph.find_neighbour(cur_data,g,count)
	con.close()
	return g

def get_data():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM users")
	users = cur.fetchall()
	con.close()
	return users

def clear_data():
	con=sql.connect("database.db")
	cur=con.cursor()
	cur.execute("DELETE from users")
	con.commit()
	con.close()

def reset_data():
	con=sql.connect('database.db')
	cur=con.cursor()
	cur.execute("DROP table if exists users")
	con.commit()
	con.close()

if __name__=='__main__':
	choice=0
	print("Create Table : ")
	choice=int(input())
	if choice==1:
		createtbl()
	d=getPaths.main()
	for i in d[:5]:
		insert_db(i[0],i[1])	
	print(get_data())

