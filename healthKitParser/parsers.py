import xml.etree.ElementTree as ET
import datetime
from record import Record

record_types = {'weight': 'HKQuantityTypeIdentifierBodyMass',
                'heart rate': 'HKQuantityTypeIdentifierHeartRate',
                'steps': 'HKQuantityTypeIdentifierStepCount'}

date_format = "%Y-%m-%d %H:%M:%S %z"

def datetime_from_string(date_string):
    """Parses a string of the date & time and returns a datetime object"""
    try:
        return datetime.datetime.strptime(date_string, date_format)
    except Exception as e:
        print("Got exception parsing date {} with format {} {}"
            .format(date_string, date_format, e))

def parse_records(file_name, record_type):
    """Parses the xml file for weight data"""

    tree = ET.parse(file_name)
    root = tree.getroot()   

    records = []

    for entry in root.findall('Record'):
        type = entry.get('type')
        if type == record_type:
            value = float(entry.get('value'))
            unit = entry.get('unit')
            source = entry.get('sourceName')
            creation_date = datetime_from_string(entry.get('creationDate'))
            start_date = datetime_from_string(entry.get('startDate'))
            end_date = datetime_from_string(entry.get('endDate'))
            
            record = Record(
                type, value, unit, source, creation_date, start_date, end_date)

            records.append(record)

    return sorted(records, key=lambda record: record.start_date)
