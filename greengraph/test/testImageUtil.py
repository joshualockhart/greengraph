from greengraph.ImageUtil import ImageUtil
from nose.tools import assert_equal
import yaml

def testIsGreen():
	img = ImageUtil()
	
	assert_equal(img.is_green(1,0,0),False)
	assert_equal(img.is_green(0,1,0),True)
