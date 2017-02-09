import xml.etree.ElementTree as ET
import datetime
from . import parser

class WeightParser(parser.Parser):
    """Class that can parse a export.xml file produced by Apple HealthKit"""

    def parse(self):
        """Parses the xml file for weight data"""
        print("Parsing {} for weight data".format(self.file_name))
        
        tree = ET.parse(self.file_name)
        root = tree.getroot()   

        data = {}
        keys = []

        for entry in root.findall('Record'):
            record_type = entry.get('type')
            if record_type == self.record_types['weight']:
                # unit = entry.get('unit')
                value = entry.get('value')
                creation_date = entry.get('startDate')
                date = self.parse_date(creation_date)

                data[date] = value # TODO: This will overwrite duplicate entries
                keys.append(date)

        keys.sort()

        for date in keys:        
            # TODO: Print in this timezone
            print("{},{}".format(date.strftime("%m/%d/%Y"), data[date]))