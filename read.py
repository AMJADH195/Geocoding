import csv
from geopy.geocoders import Nominatim
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
		except AttributeError:
			print "There's no latitude and longitude for this place"
