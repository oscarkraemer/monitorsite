#!/usr/bin/python

import os
worda = '</li> <li> <a href="'
wordb = '" tar'
wordc = worda + "http"
wordNot = "://dashb-ssb"
print "var links =["
with open("source.html") as file:
	for line in file:
		if (wordc in line) and (not wordNot in line) :
			x = line.index(worda)
                	y = line.index(wordb)
			print '"' + line[x+len(worda):y] + '", '
		else:
			continue
print "];"
