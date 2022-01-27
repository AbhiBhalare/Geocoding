#Nominatim uses OpenStreetMap data to find locations
from geopy.geocoders import Nominatim

from pprint import pprint

  
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
  
# Enter the name of location
getLoc = loc.geocode(input())
  
# printing address
print(getLoc.address)
  
# printing latitude and longitude
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)


#Get some row data of given location
app = Nominatim(user_agent="tutorial")
# get location raw data
location = app.geocode(getLoc).raw
# print raw data
pprint(location)

