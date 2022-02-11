import hashlib
from urllib.request import urlopen, Request
import filecmp
import os
from bs4 import BeautifulSoup
import numpy as np

url = Request('https://www.nrscotland.gov.uk/statistics-and-data/geography/nrs-postcode-extract',
              headers={'User-Agent': 'Moziilla/5.0'})

response = urlopen(url).read()
soup = BeautifulSoup(response)

newlink = soup.find_all("a")[36]
newlinkstr = str(newlink) # turn content into a string
#dllink = newlink['href']
newlink

with open('currentSPD.txt','w') as f:
    f.write(newlinkstr)

f1 = "./currentSPD.txt"
f2 = "./oldSPD.txt"

result = filecmp.cmp(f1, f2, shallow=False)

print(result)

if result == True:
        print('No new SPD files.')
else:
        print('Check the website for updates.')
        with open('oldSPD.txt','w') as f:
                f.write(newlinkstr)








