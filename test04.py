#! /usr/bin/python
# -*- coding:utf-8 -*-

import random
s = int(random.uniform(1,10))
print s
m = int(input('plz input a number:'))
while m != s:
	if m > s:
		print u'大了'
		m = int(input('plz input a number'))
	if m < s:
		print u'小了'                                             
		m = int(input('plz input a number'))
	if m == s:
		print('OK')
		break;
