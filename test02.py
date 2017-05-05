#! /usr/bin/python
# -*- coding:utf-8 -*-
numbers = [12,14,19,20,32]
even = []
odd = []
while len(numbers) > 0 :
	number = numbers.pop()
	if(number%2==0):
		even.append(number)
		print u'偶数：',number
	else:
		odd.append(number)
		print u'奇数：',number
