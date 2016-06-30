import suds.client
wsdl = 'http://www.webservicex.net/globalweather.asmx?wsdl'
client = suds.client.Client(wsdl)

print(client)

# cities = client.service.GetCitiesByCountry('United States')
# print(cities)

weather = client.service.GetWeather('Petersburg','United States')
print(weather)