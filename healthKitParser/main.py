import sys
import xml.etree.ElementTree as ET
import datetime
import re
import parsers.weightparser
# from parsers import weightparser

def main(file_name):
    p = parsers.weightparser.WeightParser(file_name)
    p.parse()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python weightParser.py <xml file to parse>")
        exit()
    file_name = sys.argv[1]
    main(file_name)


