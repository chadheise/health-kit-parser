import sys
import parsers
from record import Record
import matplotlib.pyplot as plt
import numpy
import pylab

def main(file_name):
    print("Parsing {} for weight data".format(file_name))
    weight_records = parsers.parse_records(
        file_name, parsers.record_types['weight'])

    for record in weight_records:
        print("{},{}".format(record.start_date, record.value))

    datetimes = [record.start_date for record in weight_records]
    weights = [record.value for record in weight_records]

    plt.plot(datetimes, weights, 'b.')
    plt.ylabel('Weight (lbs)')
    plt.xlabel("Date")
    plt.title("Weight Over Time")

    # calc the trendline
    ordinal_times = [d.toordinal() for d in datetimes]
    z = numpy.polyfit(ordinal_times, weights, 1)
    p = numpy.poly1d(z)
    pylab.plot(datetimes,p(ordinal_times),"b--")

    plt.show()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python weightParser.py <export.xml file to parse>")
        exit()
    file_name = sys.argv[1]
    main(file_name)


