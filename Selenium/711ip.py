from bs4 import BeautifulSoup
import urllib


http = urllib.urlopen()

url = 'http://nagios.philseven.com/icinga/'
response = http.request('GET', url)
response = http.request('POST', url, fields={'itdsupport':'teamstoresupport'})
#soup = BeautifulSoup(response.data)
print(response.html.data)

