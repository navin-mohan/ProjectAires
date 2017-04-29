from sklearn.preprocessing import MinMaxScaler,OneHotEncoder
import numpy as np
# from keras.models import Sequential
# from keras.layers import Dense, Activation
from datagen import generate_data


data = generate_data(300)
input_dim = 6
layer_1_dim = 4
encode_dim = 3


min_max_scalar = MinMaxScaler()
ohe = OneHotEncoder()
normal_list = []




for i in range(6):
	d = data[:, i]
	if i == 3:
		ohe.fit(np.array([[0, 1, 2, 3]]).T)
		print('------------------------------')
		print(d.reshape(1, -1).T.shape)
		print('------------------------------')
		temp = ohe.transform(d.reshape(1, -1).T).toarray()
		print(temp)
	else:
		min_max_scalar.fit(d)
		temp = min_max_scalar.transform(d).reshape(-1, 1)
	normal_list.append(temp)

normalized = np.hstack(normal_list)

# input_data = Input(shape = (input_dim, ))

# layer_1 = Dense(layer_1_dim, activation='relu')(input_data)
# encode = Dense(encode_dim, activation = 'relu')(layer_1)

# print(normalized)






