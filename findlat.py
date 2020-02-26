import csv
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
geolocator = Nominatim(user_agent='myapplication')
with open('shared_IIITMK.csv','rt')as f:
	data = csv.reader(f)
	for row in data:
		print(row[1])
		try:
			location = geolocator.geocode(row[1])
			print(location.latitude)
			print(location.longitude)
			print(location.raw)
			csvdata=[[row[1],location.latitude,location.longitude]]
			with open('newdata.csv', 'a') as csvFile:
				writer = csv.writer(csvFile)
				writer.writerows(csvdata)
		except (AttributeError,GeocoderTimedOut):
			print "There's no latitude and longitude for this place"
csvFile.close()
		