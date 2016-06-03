# File -- parser.py

'''
This module downloads the most recent list of CVE's, parses the list
and checks whether there TODO: finish this sentence........
'''

import csv

# TODO: Add this to the settings.py-file
filename = "raw-data/smallerlist.csv"

# Open the given CSV-file
def open_csv_file(filename):
    try:
        cveReader = csv.reader(open(filename, newline='\n'), delimiter=',', quotechar='"')
        return cveReader
    except FileNotFoundError:
        print("Err: The CSV-file {} cannot be found.".format(filename))

def parse_csv_file(csvobj):
    # Iterate through the list one by one
    for row in csvobj:
        if hitDetected(row):
            print(row)
            print("****************")

def hitDetected(row):
    '''
    Check whether theres is a hit in the
    crawled repository files
    '''
    # TODO: Implement this
    return True

print("Hello, I'm the parser")

csvReaderObj = open_csv_file(filename)
parse_csv_file(csvReaderObj)
