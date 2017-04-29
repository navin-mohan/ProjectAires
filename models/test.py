import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

from datagen import generate_data,normalize

min_max_scalar = MinMaxScaler()

data = generate_data(3000)

np.savetxt('3k.csv',data,delimiter=',')

min_max_scalar.fit(data)

testcase = np.array([
		[4,0,0.8,2,500],
		[0.1,0,0.8,2,500],
		[4,0,0.8,2,250],
		[4,0,0.8,2,550],

	])

# temp = min_max_scalar.transform(testcase).reshape(-1, 1)


norm_testdata = normalize(testcase,3000)
norm_data 	  = normalize(data,3000)
model = load_model('94.h5')

print(np.sum(abs(model.predict(norm_testdata) - norm_testdata),axis=1))
# print(np.mean(np.sum(abs(model.predict(norm_data) - norm_data),axis=1)))




