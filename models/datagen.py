import numpy as np

SIZE = 30

np.random.seed(10)

visibility = np.abs(np.random.normal(loc=2.0,scale=1.5,size=SIZE))
age		   = np.abs(np.random.normal(loc=44,scale=20,size=SIZE)).astype(np.integer)
weather	   = np.append(np.random.choice(np.array([0,1]),int(SIZE*0.99)), np.random.choice(np.array([2,3]),int(SIZE*0.01)))

if weather.shape[0] != SIZE:
	# print("size:",SIZE-weather.shape[0])
	weather = np.append(weather,np.random.choice(np.array([0,1,2,3]),SIZE-weather.shape[0])) 

road_quality = np.abs(np.random.normal(loc=0.3,scale=1,size=SIZE))
accelerometer = np.abs(np.random.normal(loc=2.2,scale=1,size=SIZE))
speed		= 2*np.multiply(road_quality,np.random.normal(loc=60,scale=0.1,size=SIZE)) + np.random.uniform(low=0,high=10,size=SIZE)


dataset = np.array([
		visibility,
		age,
		weather,
		road_quality,
		accelerometer,
		speed
	])

# print(visibility.shape,age.shape,weather.shape,road_quality.shape,accelerometer.shape,speed.shape)
print(dataset.T.astype(np.float32))

