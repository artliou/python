import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

source = '''
<comments>
<comment>
<name>Oriane</name>
<count>98</count>
</comment>
<comment>
<name>Nerisse</name>
<count>91</count>
</comment>
<comment>
<name>Marwan</name>
<count>90</count>
</comment>
<comment>
<name>Ashleen</name>
<count>90</count>
</comment>
<comment>
<name>Kerri</name>
<count>88</count>
</comment>
<comment>
<name>Fathima</name>
<count>85</count>
</comment>
<comment>
<name>Ashleigh</name>
<count>83</count>
</comment>
<comment>
<name>Laaibah</name>
<count>83</count>
</comment>
<comment>
<name>Anika</name>
<count>82</count>
</comment>
<comment>
<name>Makensie</name>
<count>79</count>
</comment>
<comment>
<name>Abdisalam</name>
<count>76</count>
</comment>
<comment>
<name>Kasi</name>
<count>71</count>
</comment>
<comment>
<name>Kealon</name>
<count>71</count>
</comment>
<comment>
<name>Sophie</name>
<count>61</count>
</comment>
<comment>
<name>Gabby</name>
<count>58</count>
</comment>
<comment>
<name>Sebastien</name>
<count>55</count>
</comment>
<comment>
<name>Riana</name>
<count>55</count>
</comment>
<comment>
<name>Kalen</name>
<count>52</count>
</comment>
<comment>
<name>Steve</name>
<count>50</count>
</comment>
<comment>
<name>Rowan</name>
<count>50</count>
</comment>
<comment>
<name>Lovell</name>
<count>50</count>
</comment>
<comment>
<name>Anne</name>
<count>49</count>
</comment>
<comment>
<name>Mehek</name>
<count>48</count>
</comment>
<comment>
<name>Tira</name>
<count>45</count>
</comment>
<comment>
<name>Mathu</name>
<count>44</count>
</comment>
<comment>
<name>Nelly</name>
<count>44</count>
</comment>
<comment>
<name>Abid</name>
<count>41</count>
</comment>
<comment>
<name>Jazeb</name>
<count>41</count>
</comment>
<comment>
<name>Filip</name>
<count>40</count>
</comment>
<comment>
<name>Sohan</name>
<count>40</count>
</comment>
<comment>
<name>Jostelle</name>
<count>37</count>
</comment>
<comment>
<name>Kajally</name>
<count>36</count>
</comment>
<comment>
<name>Abir</name>
<count>35</count>
</comment>
<comment>
<name>Rae</name>
<count>34</count>
</comment>
<comment>
<name>Kaelyn</name>
<count>32</count>
</comment>
<comment>
<name>Gregory</name>
<count>29</count>
</comment>
<comment>
<name>Tadd</name>
<count>28</count>
</comment>
<comment>
<name>Ruaidhri</name>
<count>27</count>
</comment>
<comment>
<name>Jaymie</name>
<count>27</count>
</comment>
<comment>
<name>Guy</name>
<count>25</count>
</comment>
<comment>
<name>Lotti</name>
<count>21</count>
</comment>
<comment>
<name>Tansy</name>
<count>19</count>
</comment>
<comment>
<name>Marlin</name>
<count>19</count>
</comment>
<comment>
<name>Ayla</name>
<count>18</count>
</comment>
<comment>
<name>Rheanna</name>
<count>17</count>
</comment>
<comment>
<name>Sacha</name>
<count>12</count>
</comment>
<comment>
<name>Yaseen</name>
<count>8</count>
</comment>
<comment>
<name>Emmylou</name>
<count>4</count>
</comment>
<comment>
<name>Kalani</name>
<count>2</count>
</comment>
<comment>
<name>Chantelle</name>
<count>1</count>
</comment>
</comments>
'''

root = ET.fromstring(source)
levels = root.findall('.//comment')
# print(levels)
total = 0
for level in levels:
    count = level.find('count').text
    print(count)
    count = int(count)
    total += count

print("Counts:", total)

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break

#     parms = dict()
#     parms['address'] = address
#     if api_key is not False: parms['key'] = api_key
#     url = serviceurl + urllib.parse.urlencode(parms)
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)

#     data = uh.read()
#     print('Retrieved', len(data), 'characters')
#     print(data.decode())
#     tree = ET.fromstring(data)

#     # results = tree.findall('result')
#     counts = tree.findall('.//count')
#     # name = counts[0].find('comment').find('name').text
#     # count = counts[0].find('comment').find('count').text
#     # location = counts[0].find('formatted_address').text
#     print("Counts:", counts)
#     # print('lat', lat, 'lng', lng)
#     # print(location)
