from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='myapplication')
location = geolocator.geocode("Piravanthur")
print(location.latitude)
print(location.longitude)
print(location.address)
print(location.raw)

# Kulasekharapuram
