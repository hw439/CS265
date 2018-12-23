#!/usr/bin/env python3
#Kevin Wong
#kmw396 - 14240214
#10/28/2018
#Lab 5 - Python Intro - Q2
#Imports UTF-8 file ids, removes whitespace and splits name from number, sorts name and numbers, and prints output

import sys

if len(sys.argv) == 1:
	print("Missing Arguments")
	sys.exit()
else:
	f = open(sys.argv[1], "r") #open file
	
d = {} #dictionary

read = f.readline()
while read:
	read = read.strip("\n") #remove whitespace
	split = read.split(" ", 1) #split name from number
	d[int(split[0])] = split[1] #add record to dictionary
	read = f.readline() #read next line
		
for key in sorted(d): #print output
	print('{0} {1}'.format(key, d[key]))
