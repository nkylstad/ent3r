"""
Script for making a long list of temperatures and writing them all to file.
User can decide whether to use fahrenheit or celcius on the command line.
"""

import sys
from numpy import *

N = 365  # Days in a year

try:
	degree_type = raw_input("Please choose Celcius (C) or Fahrenheit (F)")
	if degree_type == "C":  # Choose realistic values for temperatures
		temperatures = random.random_integers(-20,45,N)

