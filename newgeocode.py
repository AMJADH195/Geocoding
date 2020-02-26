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
			print(location.address)
			print(location.raw)
			csvdata=[[row[0],row[1],location.latitude,location.longitude,location.address]]
			with open('address1.csv', 'a') as csvFile:
				writer = csv.writer(csvFile)
				writer.writerows(csvdata)
		except (AttributeError,GeocoderTimedOut):
			with open('address1.csv', 'a') as csvFile2:
				csvdata2=[[row[0],row[1],"no latitude found","no longitude found","no address found"]]
				writer = csv.writer(csvFile2)
				writer.writerows(csvdata2)
			
csvFile.close()
		
