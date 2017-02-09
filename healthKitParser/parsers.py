import xml.etree.ElementTree as ET
import datetime

record_types = {'weight': 'HKQuantityTypeIdentifierBodyMass'}

date_format = "%Y-%m-%d %H:%M:%S %z"

def datetime_from_string(date_string):
    """Parses a string of the date & time and returns a datetime object"""
    try:
        return datetime.datetime.strptime(date_string, date_format)
    except Exception as e:
        print("Got exception parsing date {} with format {} {}"
            .format(date_string, date_format, e))

def parse_weight(file_name):
    """Parses the xml file for weight data"""
    print("Parsing {} for weight data".format(file_name))
    
    tree = ET.parse(file_name)
    root = tree.getroot()   

    data = {}
    keys = []

    for entry in root.findall('Record'):
        record_type = entry.get('type')
        if record_type == record_types['weight']:
            # unit = entry.get('unit')
            value = entry.get('value')
            creation_date = entry.get('startDate')
            date = datetime_from_string(creation_date)

            data[date] = value # TODO: This will overwrite duplicate entries
            keys.append(date)

    keys.sort()

    for date in keys:        
        # TODO: Print in this timezone
        print("{},{}".format(date.strftime("%m/%d/%Y"), data[date]))

    return data # TODO: Consider a custom data type


