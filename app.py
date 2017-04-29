from flask import Flask
import numpy as np 
from anomaly import Anomaly 

app  = Flask(__name__)

@app.route('/')
def index():
	a = Anomaly()

	testcase = np.array([
			[4,0,0.8,2,500],
			[0.1,0,0.8,2,500],
			[4,0,0.8,2,250],
			[4,0,0.8,2,550],

		])

	total = a.get_anomaly(testcase)
	mean = a.get_mean_anomaly(testcase)
	contributer = a.get_largest_contributer(testcase)

	# print("total anomaly:",)
	# print("avg anomaly:",)
	# print("contributer:",a.get_largest_contributer(testcase))

	return "<br/>".join(["total anomaly: {0} <br/> mean anomaly: {1} <br/> contributer: {2}".format(x,y,z) for x,y,z in zip(total,mean,contributer)])


if __name__ == '__main__':
	app.run(debug=True)
