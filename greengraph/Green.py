from GeoUtil import GeoUtil
from ImageUtil import ImageUtil
class Green(object):
    def __init__(self):
        self.geoUtil = GeoUtil()
        self.imgUtil = ImageUtil()

    def getGreenMapOfLocation(self,location):
        locationString = self.geoUtil.geolocate(location)
        return self.imgUtil.show_green_in_png(self.geoUtil.map_at(*locationString, zoom=10,satellite=True))

    def getGreenValuesBetweenTwoLocations(self, locationA, locationB):
        vals = [self.imgUtil.count_green_in_png(self.geoUtil.map_at(*location,zoom=10,satellite=True))
            for location in self.geoUtil.location_sequence(
                self.geoUtil.geolocate(locationA),
                self.geoUtil.geolocate(locationB),
                10)]
        return vals
