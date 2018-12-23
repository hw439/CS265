#!/usr/bin/env python3
#Kevin Wong
#kmw396 - 14240214
#10/28/2018
#Lab 5 - Python Intro - Q1
#Imports students.csv, splits name/grade and removes "," from csv file, calculate avg, print output

import sys
import math

if sys.argv[1] == 'students.csv': #arg checking

	f = open( sys.argv[1], "r" ) # open file

	read = f.readline() # open file line by line into read var
	while read:
		split = read.split(",") #split each line into parts and remove ","
		length = len(split[1:]) #store the length of the digits into length var
		i = 1
		total = 0 #total of student scores
		while i<=length: 
			total += float(split[i]) # increment total
			i += 1
		total = int(round(total/length))
		print('{0} {1}'.format(split[0], total)) #print and format
		read = f.readline() #read next line of file
