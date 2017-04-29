from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder

import numpy as np


class Anomaly():

	def __init__(self):
		self.model = load_model('models/983k.h5')
		self.traindata = np.genfromtxt('models/3k.csv',delimiter=',')
		self.min_max_scalar = MinMaxScaler()
		self.ohe = OneHotEncoder()
		self.ohe.fit(np.array([[0, 1, 2, 3]]).T)


	def normalize(self,data):
		normalized_data = []

		for i in range(self.traindata.shape[1]):
			d = self.traindata[:,i]
			d1 = data[:,i]
			if i == 2:
				temp = self.ohe.transform(d1.reshape(1, -1).T).toarray()
			else:
				self.min_max_scalar.fit(d)
				temp = self.min_max_scalar.transform(d1).reshape(-1, 1)
			normalized_data.append(temp)
		return np.hstack(normalized_data)

	def get_anomaly(self,Y):
		norm_Y = self.normalize(Y)
		return np.sum(np.abs(self.model.predict(norm_Y) - norm_Y),axis=1)

	def get_mean_anomaly(self,Y):
		norm_Y = self.normalize(Y)
		return np.mean(np.abs(self.model.predict(norm_Y) - norm_Y),axis=1)

	def get_largest_contributer(self,Y):
		norm_Y = self.normalize(Y)
		return np.argmax(np.abs(self.model.predict(norm_Y) - norm_Y),axis=1)		

