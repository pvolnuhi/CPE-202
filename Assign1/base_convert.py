#
#Polina Volnuhina
#014302388
#4/06/2019
#
#Assignment 1
#CPE 202-13
#taking in strings made up of letters and generating all the permutations possible 
#for the arrangement of that string.
#a recursive function that takes a non-negative integer num (base 10) and a base b (integer from 2 to 16) 
#and returns a string representing the base b number:

def convert(num, b):
	"""Recursive function that returns a string representing num in the base b"""
	if (num != int(num)):
		return str(num)

	if (num <= 1):   #checks to see that num is non-negative integer
		return str(num)


	elif (b < 2 or b > 16):   #checks to see if out of bounds
		return str(b)

	else:
		quotient = num//b
		alpha = '0123456789ABCDEF'
		remainder = num % b
		return str(convert(quotient,b)) + alpha[remainder]	