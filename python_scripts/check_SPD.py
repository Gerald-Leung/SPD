import hashlib
import urllib
import urllib.request
from urllib.request import urlopen, Request
import filecmp
import os
from bs4 import BeautifulSoup
import numpy as np
import wget
import requests
import zipfile
import io
import argparse

'''Script to download updated SPD Files
from the National Records of Scotland 
website.'''
'''NOTE: You may have to disconnect your
VPN for this script to work.'''

# Access the url and create 
#a BeautifulSoup object
url = Request('https://www.nrscotland.gov.uk/statistics-and-data/geography/nrs-postcode-extract',
        headers={'User-Agent': 'Moziilla/5.0'})
response = urlopen(url).read()
soup = BeautifulSoup(response,"html.parser")

# Find our target link
def search_link(response_object,tag,date):

    k = BeautifulSoup(response_object,"html.parser")
    a = k.find_all('{}'.format(tag),
            text='{0}'.format(date))
    #b = k.find_all('{0}'.format(tag))
    
    return a

a = "a"
parse_date = argparse.ArgumentParser()
parse_date.add_argument('--date', type=str,
        required=True)
date_arg = parse_date.parse_args()
#b = "2021-2"
#print("{0},text={1}".format(a,b))
x = search_link(response,a,date_arg.date)
print(x)
#z = soup.find_all("{0},text={1}".format(a,b))
#print(z)

t1 = x[1].string
print(t1)

# Check for updates
with open('currentSPD.txt','w') as f:
    f.write(t1)

f1 = "./currentSPD.txt"
f2 = "./oldSPD.txt"
result = filecmp.cmp(f1,f2,shallow=False)
print(result)

if result == True:
    print('No new SPD files since last checked.')
else:
    print('Check the website for updates.')
    print('=============================')
    print('Proceeding with download.')
    print('=============================')
    print('\n')
    
    with open('oldSPD.txt','w') as f:
        f.write(t1)

    base_target = "https://www.nrscotland.gov.uk"
    target_linkhref = x[1]["href"]
    target_url = base_target+target_linkhref
    print(target_url)

    get_target_url = Request(target_url,
            headers={'User-Agent': 'Moziilla/5.0'})
    target_html = urlopen(get_target_url).read()
    target_soup = BeautifulSoup(target_html,'html.parser')
    file_target = target_soup.find_all(
            'a',text='Postcode Index')[1]['href']
    print(file_target)










