import urllib
import urllib.request
import json
import polyline


url_str ='https://maps.googleapis.com/maps/api/directions/json?units=metric&origin=%s&destination=%s&alternatives=true&mode=driving'
header = {
			'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			'Accept-Encoding': 'none',
			'Accept-Language': 'en-US,en;q=0.8',
			'Connection': 'keep-alive'
}

def getPaths(source,destination):
	return_data = []
	source = ','.join(source)
	destination = ','.join(destination)
	url = url_str%(source,destination)
	req = urllib.request.Request(url, headers=header) 
	data_str = urllib.request.urlopen(req).read()
	data = json.loads(data_str)
	routes = data['routes']
	for route in routes:
		polyLineEnc = route['overview_polyline']['points']
		points = polyline.decode(polyLineEnc)
		return_data.append(points)

	return return_data




def main():
	return (getPaths( ('10.05839','76.3579399'),('10.0159','76.3419') )[0])
