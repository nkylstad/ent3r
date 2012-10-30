"""
Script for extracting data from a data file copied from 
http://www.yr.no/place/Norway/Oslo/Oslo/Oslo/detailed_statistics.html
Use average temperatures, which are in the 3rd temperature column.
"""

import sys

try:
	filename = sys.argv[1]
except:
	print "Please enter valid filename on command line."
	sys.exit(1)

try:
	f = open(filename, 'r')
except:
	print "File not found."
	sys.exit(1)

dates = []
temperatures = []

for line in f:
	temporary_list = []
	data = line.split()
	for i in range(3):
		temporary_list.append(data[i])
	dates.append(temporary_list)
	temperatures.append(data[5])


