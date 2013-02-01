#!/usr/bin/python

import random

def randplace(number, latmin, latmax, longmin, longmax):
    for num in range(1, number):

        latitude = random.uniform(latmin, latmax)
        longitude = random.uniform(longmin, longmax)
        latitude = 46
        longitude = 16
        kml = (
           '<Placemark>\n'
           '<name>Radio Information Recipient</name>\n'
           '<Point>\n'
           '<coordinates>%f,%f</coordinates>\n'
           '</Point>\n'
           '</Placemark>\n'
           ) %(longitude, latitude)
        print kml

print '<?xml version="1.0" encoding="UTF-8"?>'
print '<kml xmlns="http://www.opengis.net/kml/2.2">'
print '<Document>'

print '</Document>'
print '</kml>'
