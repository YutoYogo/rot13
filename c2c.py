#	Project	:	c2c
#	File	:	c2c.py
#	Author	:	Yuto Arisaka
#	Since	:	Wed Nov 17 22:37 2021
#	Update	:	none
#	Coding	:	UTF-8

import csv

memory = ""
original = input("Enter your text: ")
container = list(original)

file = open("c2c.csv", "r", encoding="utf-8")
data = csv.reader(file)
data = [ divide for divide in data ]
datadic = dict(data)
file.close()

for char in container:
	if char in datadic:
		memory += datadic[char]
	else:
		memory += char

print("Translation Result: ", memory)
