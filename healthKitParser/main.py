import sys
import parsers

def main(file_name):
    p = parsers.parse_weight(file_name)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python weightParser.py <xml file to parse>")
        exit()
    file_name = sys.argv[1]
    main(file_name)


