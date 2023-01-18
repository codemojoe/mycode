#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import time
#import reverse_geocoder as rg

URL = "http://api.open-notify.org/iss-now.json"

def main():
    response = requests.get(URL).json()

    print(response)

    timestamp = response['timestamp']
    humantime = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(timestamp))
    print(timestamp)
    print(humantime)

    pos = response['iss_position']
    lat = pos['latitude']
    lon = pos['longitude']

    # reverse_geocoder MUST be passed a tuple as the argument!
    #coords_tuple= (lat, lon)
    #result = rg.search(coords_tuple, verbose=False)

    print(f"CURRENT LOCATION OF THE ISS: ")
    print(f"Timestamp: {humantime}") 
    print(f"Lon: {lon}")
    print(f"Lat: {lat}")
    #print(f"City/Country: {result}")


if __name__ == "__main__":
    main()
