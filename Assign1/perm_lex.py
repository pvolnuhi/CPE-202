#
#Polina Volnuhina
#014302388
#4/06/2019
#
#Assignment 1
#CPE 202-13
#taking in strings made up of letters and generating all the permutations possible 
#for the arrangement of that string.
import sys

def perm_gen_lex(a):

	add_to_list = []  #checks empty string, returns emtpy list
	if len(a) == 0:
		return []

	if len(a) == 1:   #checks when length is exactly one
		return [a]
	elif len(a) == 2:
		return [a,a[::-1]]
	
	#take first char
	c = a[0]
	#call function recursively on the rest of the string : a[1:]
	rest = a[1:]
	
	perms = perm_gen_lex(rest)

	for perm in perms:
		add_to_list.extend(single_perm(c, perm))
	add_to_list.sort()
	return add_to_list

def single_perm(c, perm):
	result = []
	for i in range(len(perm)):
		result.append(perm[:i] + c + perm[i:])
	result.append(perm+c)
	return result

# def main(argv):
# 	perm = perm_gen_lex("abc")
# 	print(perm)

# if __name__ == "__main__":
#         main(sys.argv)
