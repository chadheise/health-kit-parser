import sys
import parsers
from record import Record

def main(file_name):
    print("Parsing {} for weight data".format(file_name))
    weight_records = parsers.parse_weight(file_name)

    for record in weight_records:
        print("{},{}".format(record.start_date, record.value))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python weightParser.py <export.xml file to parse>")
        exit()
    file_name = sys.argv[1]
    main(file_name)


