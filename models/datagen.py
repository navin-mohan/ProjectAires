import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder


def normalize(data,batch_size,seed=10):
	min_max_scalar = MinMaxScaler()
	ohe = OneHotEncoder()
	normal_list = []

	ohe.fit(np.array([[0, 1, 2, 3]]).T)

	traindata = generate_data(batch_size,seed)


	for i in range(6):
		d = traindata[:, i]
		d1 = data[:,i]
		if i == 3:
			temp = ohe.transform(d1.reshape(1, -1).T).toarray()
			print(temp)
		else:
			min_max_scalar.fit(d)
			temp = min_max_scalar.transform(d1).reshape(-1, 1)
		normal_list.append(temp)

	return np.hstack(normal_list)


def generate_data(batch_size,seed=10):

	np.random.seed(seed)
	SIZE = batch_size
	visibility = np.abs(np.random.normal(loc=2.0,scale=1.5,size=SIZE))
	age		   = np.abs(np.random.normal(loc=44,scale=20,size=SIZE)).astype(np.integer)
	weather	   = np.append(np.random.choice(np.array([0,1]),int(np.floor(SIZE*0.99))), np.random.choice(np.array([2,3]),int(np.ceil(SIZE*0.01)))) 
	road_quality = np.abs(np.random.normal(loc=0.3,scale=1,size=SIZE))
	accelerometer = np.abs(np.random.normal(loc=2.2,scale=1,size=SIZE))
	speed		= 2*np.multiply(road_quality,np.random.normal(loc=60,scale=0.1,size=SIZE)) + np.random.uniform(low=0,high=10,size=SIZE)


	return  np.array([
			visibility,
			age,
			weather,
			road_quality,
			accelerometer,
			speed
		]).T.astype(np.float32)


print(generate_data(300)[0])

