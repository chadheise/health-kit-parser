import sys
import parsers
from record import Record
import matplotlib.pyplot as plt
import numpy
import pylab
import datetime

def main(file_name, start_date_string):
    print("Parsing {} for weight data".format(file_name))
    weight_records = parsers.parse_records(
        file_name, parsers.record_types['weight'])

    for record in weight_records:
        print("{},{}".format(record.start_date, record.value))

    datetimes = [record.start_date for record in weight_records]
    weights = [record.value for record in weight_records]

    if start_date_string:
        # Filter times by start date
        timezone = datetime.timezone(datetime.timedelta(hours=-8))
        start = datetime.datetime.strptime(start_date_string, '%m/%d/%Y') \
            .replace(tzinfo=timezone)
        start_index = getStartIndex(datetimes, start)
        datetimes = datetimes[start_index:]
        weights = weights[start_index:]

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

# Assumes a sorted list
def getStartIndex(datetimes, start_date=None):
    if start_date == None:
        return 0

    for i in range(0, len(datetimes)):
        if datetimes[i] > start_date:
            return i - 1
    return len(datetimes)

if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage: python weightParser.py <export.xml file to parse> " + 
             "<start date>")
        exit()
    file_name = sys.argv[1]

    start_date = None
    if (len(sys.argv) > 2):
        start_date = sys.argv[2]
    main(file_name, start_date)


