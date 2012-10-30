"""
Celcius-to-Fahrenheit or Fahrenheit-to-Celcius converter.
"""
import sys

def find_degree_type():
	degrees = raw_input("Would you like to convert to Celcius (C) or to Fahrenheit (F)? (type \'quit\' to exit.)  ")
	if degrees == "C":
		convert_to_C()
	elif degrees == "F":
		convert_to_F()
	elif degrees == "quit":
		print "Exiting. Goodbye!"
		sys.exit(1)
	else:
		print "Error. Please try again."
		find_degree_type()

def convert_to_C():
	temperature = float(raw_input("Please enter a temperature in Fahrenheit:  "))
	temp_C = 5.0/9*(temperature - 32)
	print "degrees Fahrenheit:  ", temperature
	print "degrees Celcius:  ", temp_C
	print " "
	find_degree_type()

def convert_to_F():
	temperature = float(raw_input("Please enter a temperature in Celcius:  "))
	temp_F = 9.0/5*temperature + 32
	print "degrees Celcius:  ", temperature
	print "degrees Fahrenheit:  ", temp_F
	print " "
	find_degree_type()


find_degree_type()