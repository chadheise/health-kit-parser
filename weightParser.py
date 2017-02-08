import sys
import xml.etree.ElementTree as ET
import datetime
import re

def parse(file_name):
    """Parses the xml file defined by the fileName."""
    print("Parsing " + file_name)  
    
    record_types = {}
    record_types["weight"] = "HKQuantityTypeIdentifierBodyMass"

    tree = ET.parse(file_name)
    root = tree.getroot()   

    for entry in root.findall('Record'):
        # rank = country.find('rank').text
        # name = country.get('name')
        record_type = entry.get('type')
        if record_type == record_types["weight"]:
            unit = entry.get('unit')
            value = entry.get('value')
            creation_date = entry.get('creationDate')
            date = parse_date(creation_date)
            print(value + " " + unit + " " + creation_date)

def parse_date(date_string):
    try:
        date_format = "%Y-%m-%d %H:%M:%S %z"
        date = datetime.datetime.strptime(date_string, date_format)
        return date
    except Exception as e:
        print("Got exception parsing date {} with format {} {}".format(date_string, date_format, e))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python weightParser.py <xml file to parse>")
        exit()
    file_name = sys.argv[1]
    parse(file_name)


