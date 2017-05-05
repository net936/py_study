#! /usr/bin/python
import re

line = "cates are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line , re.M|re.I)

if(matchObj):
	print "match :",matchObj.group()
	print "match 1: ",matchObj.group(1)
	print "match 2: ",matchObj.group(2)
else:
	print "no match"