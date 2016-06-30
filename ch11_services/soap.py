import suds.client
wsdl = 'http://www.webservicex.net/globalweather.asmx?wsdl'
svc = suds.client.Client(wsdl).service

print(svc)

# cities = client.service.GetCitiesByCountry('United States')
# print(cities)

weather = svc.GetWeather('Petersburg', 'United States')
print(weather)