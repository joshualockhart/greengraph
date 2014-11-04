from ImageUtil import ImageUtil
from GeoUtil import GeoUtil
from Green import Green
import png
from argparse import ArgumentParser

def process():
    parser = ArgumentParser(description = "Look for green stuff")
    parser.add_argument('cityOne')
    parser.add_argument('--cityTwo')
    arguments= parser.parse_args()

    green = Green()
    if arguments.cityTwo != None:
        vals = green.getGreenValuesBetweenTwoLocations(arguments.cityOne,arguments.cityTwo)
    
        import matplotlib.pyplot as plt
    
        plt.plot(vals)
    
        plt.savefig('greengraph.png')
    
    else:
        with open('green.png','w') as g:
            g.write(green.getGreenMapOfLocation(arguments.cityOne))

if __name__ == "__main__":
    process()