from greengraph.GeoUtil import GeoUtil
from nose.tools import assert_equal
import yaml

def testGeoLocate():
	g = GeoUtil()
	
	assert_equal(g.geolocate("Belfast"), (54.59728500000001, -5.93012))
	assert_equal(g.geolocate("London"), (51.5073509, -0.1277583))
	
testGeoLocate()