import geopy
import requests
from numpy import linspace

class GeoUtil(object):
    def __init__(self):
        self.geocoder = geopy.geocoders.GoogleV3(domain="maps.google.co.uk")

    def geolocate(self, place):
        return self.geocoder.geocode(place,exactly_one=False)[0][1]

    def map_at(self, lat, long, satellite=False, zoom=12, size=(400,400), sensor=False):
        base="http://maps.googleapis.com/maps/api/staticmap?"
        params=dict(
            sensor= str(sensor).lower(),
            zoom= zoom,
            size= "x".join(map(str,size)),
            center= ",".join(map(str,(lat,long))),
            style="feature:all|element:labels|visibility:off"
        )
        if satellite:
            params["maptype"]="satellite"
        return requests.get(base,params=params)

    def location_sequence(self, start,end,steps):
        # Would actually prefer this if steps
        # were deduced from zoomlevel
        # But need projection code for that
        lats=linspace(start[0],end[0],steps)
        longs=linspace(start[1],end[1],steps)
        return zip(lats,longs)

