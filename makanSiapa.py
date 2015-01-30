#!/usr/bin/python

import urllib, json, datetime, sys

kota = str(sys.argv[1])
url = "http://api.openweathermap.org/data/2.5/weather?q=" 
resp = urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q= %s" % kota)
data = json.loads(resp.read())

d = datetime.datetime.now()

if ( d.hour > 5 and d.hour <= 10):
    if(data["main"]["temp"] - 273 < 24):
        print "Bubur Ayam"
    else:
        print "Jus Jeruk"
elif ( d.hour > 10 and d.hour <= 14):
    if(data["main"]["temp"] - 273 < 22):
        print "Soto Ayam" 
    else:
        print "Sop Buah"
elif ( d.hour > 14 and d.hour <= 18):
    if(data["main"]["temp"] - 273 < 24):
        print "Bakso"
    else:
        print "Eskrim"
else:
    if(data["main"]["temp"] - 273 < 24):
        print "Bakso"
    else:
        print "Eskrim"
        
