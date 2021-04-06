# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count: ') #how many times this repeats
position = input('Enter position: ')
count = float(count)
position = float(position)
processCount = 0


def search(url, position):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    counter = 0
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        counter += 1
        print(tag.get('href', None))
        if counter == position:
                print("FOUND")
                return tag.get('href', None)

while processCount < count:
    url = search(url, position)
    processCount += 1

# Now at the Count
print(url)
