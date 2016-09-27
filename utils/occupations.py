#!/usr/bin/python
# OG & SY
# SoftDev pd. 8

from data import occupations
import csv
import random



def giveMeADictionary():
	d = {}
	with open('occupations.csv') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if (row[0] != "Job Class" and row[0] != "Total"):
				d[row[0]] = row[1]
                        		
'''for key in d.keys():
        print key + ": "+ d[key]'''


def givMeAJob(d):
	li = []
	for x in d.keys():
		for i in range( int(float(d[x]) * 10)):
			li.append(x)
        return random.choice(li)


csvfile.close()
