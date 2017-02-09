import xml.etree.ElementTree as ET
import datetime

class Parser:
    """Class that can parse a export.xml file produced by Apple HealthKit"""

    record_types = {}
    record_types['weight'] = "HKQuantityTypeIdentifierBodyMass"

    def __init__(self, file_name):
        self.file_name = file_name

    def parse_date(self, date_string):
        try:
            date_format = "%Y-%m-%d %H:%M:%S %z"
            return datetime.datetime.strptime(date_string, date_format)
        except Exception as e:
            print("Got exception parsing date {} with format {} {}"
                .format(date_string, date_format, e))