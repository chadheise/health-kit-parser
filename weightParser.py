import sys
import xml.etree.ElementTree as ET

def parse(fileName):
    """Parses the xml file defined by the fileName."""
    print(fileName + " woah")  
    tree = ET.parse(fileName)
    root = tree.getroot()      

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python weightParser.py <xml file to parse>")
        exit()
    fileName = sys.argv[1]
    print(fileName)
    parse(fileName)


