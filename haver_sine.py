import numpy as np

def calc_dist(la_one,la_two,lo_one,lo_two):
  rad_earth=6371
  d_la = np.radians(la_two-la_one)
  d_lo = np.radians(lo_two-lo_one) 
  a = np.sin(d_la/2)*np.sin(d_la/2)+np.cos(np.radians(la_one))*np.cos(np.radians(la_two))*np.sin(d_lo/2)*np.sin(d_lo/2)
  c = 2*np.arctan2(np.sqrt(a),np.sqrt(1-a)) 
  d = rad_earth*c
  return d;


if __name__=='__main__':
	for i in range(1,100):
		res=calc_dist(43.5,45.5,43.5,45.5)
		print(res)
