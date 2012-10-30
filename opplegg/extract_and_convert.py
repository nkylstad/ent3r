# -*- coding: utf-8 -*-
"""
Script for extracting data from a data file copied from 
http://www.yr.no/place/Norway/Oslo/Oslo/Oslo/detailed_statistics.html
Use average temperatures, which are in the 3rd temperature column.
"""
import sys
from numpy import *
from matplotlib import pyplot

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
temperature_list = []

for line in f:
	temporary_list = []
	data = line.split()
	for i in range(3):
		temporary_list.append(data[i])
	dates.append(temporary_list)
	temperature = float(data[5].strip('°'))
	temperature_list.append(temperature)

temperature_list.reverse()
temperatures = array(temperature_list)

savetxt("temp_list.txt", temperatures)


