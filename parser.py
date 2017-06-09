#!/usr/bin/python
import json

lines = open("finalPsych.txt").readlines()

guide = {}
newSection = True
curline = ""

for line in lines:
	if line == '\n':
		newSection = True
		continue

	line = line.replace('\n','')

	if newSection:
		curline = line.replace('\n','')
		guide[curline] = []
		newSection = False
		continue

	guide[curline].append(line)

advanced_guide = {}

for section in guide:
	print "==================================================="
	print section
	advanced_guide[section] = {}
	for idea in guide[section]:
		print "Provide ideas related to: "
		print idea + ": "
		advanced_guide[section][idea] = []
		i = 1
		response = raw_input(str(i)+". ")
		while response:
			i += 1
			advanced_guide[section][idea].append(response)
			response = raw_input(str(i)+". ")
		print " "

output = json.dumps(advanced_guide)

filename = "output.json"
target = open(filename, 'w')
target.truncate()
target.write(output)
target.close()