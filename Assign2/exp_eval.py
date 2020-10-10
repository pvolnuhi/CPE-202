#
#Polina Volnuhina
#014302388
#4/24/2019
#
#Assign2 
#CPE 202-13
#Practising evaluations using precedence and left or right association of operations

import sys
from stack_array import Stack

class PostfixFormatException(Exception):     	
	pass
	
class Dict:
	value = {"-": [1,0], "+": [1,0], "/": [2,0], "*": [2,0], "**": [3,1], ">>": [4,0], "<<": [4,0]}
	

def infix_to_postfix(input_str):   #CALL DICT HELPER FUNCTION HERE 
	"""Converts an infix expression to an equivalent postfix expression """

	"""Input argument:  a string containing an infix expression where tokens are 
	space separated. Tokens are either operators + - * / ^ parentheses ( ) or numbers
	Returns a String containing a postfix expression """
	stack_ = Stack(50)
	RPN_list = []
	string_to_list = input_str.split()
	for i in string_to_list:
		if is_number(i):  
			RPN_list.append(i)
		elif i == ")":
			while not stack_.is_empty() and stack_.peek() != "(":
				RPN_list.append(stack_.pop()) #pop operators off the stack
			stack_.pop() # pop "("  
		elif i == "(":
			stack_.push("(") #don't put in RPN_list expression
		elif is_operator(i):
			while not stack_.is_empty() and is_operator(stack_.peek()):
				op = stack_.peek()
				if left_associative(i) and less_than_or_equals(i, op) or \
					right_associative(i) and less_than(i, op):
					RPN_list.append(stack_.pop())
				else:
					break

			stack_.push(i)		

	while not stack_.is_empty():
		RPN_list.append(stack_.pop())
	
	return " ".join(str(x) for x in RPN_list) #concatenate strings 

def left_associative(op):
	return Dict.value[op][1] == 0

def right_associative(op):
	return not left_associative(op)

def less_than_or_equals(op1, op2):
	return Dict.value[op1][0] <= Dict.value[op2][0]

def less_than(op1, op2):
	return Dict.value[op1][0] < Dict.value[op2][0] #checking for the '**'	

def postfix_eval(input_str):  #ACCOUNT FOR ERRORS 
	"""Evaluates a postfix expression"""
	"""Input argument:  a string containing a postfix expression where tokens 
	are space separated.  Tokens are either operators + - * / ^ or numbers
	Returns the result of the expression evaluation. 
	Raises an PostfixFormatException if the input is not well-formed"""
	stack_ = Stack(30)
	postfix_list = input_str.split() #converts string to list 
	if postfix_list is None:
		raise PostfixFormatException("Insufficient operands")
	keys = [*Dict.value] 
	for i in postfix_list:
		if i not in keys: 
			if is_number(i):
				stack_.push(i)
			else:
				raise PostfixFormatException("Invalid token")	
		else: 
			if (stack_.size() < 2):
				raise PostfixFormatException("Insufficient operands")
			op1 = stack_.pop()
			op2 = stack_.pop()
			if i in [">>", "<<"]:
				if not valid_ints(op1, op2):
					raise PostfixFormatException('Illegal bit shift operand') 
				else:
					stack_.push(str(math_oper(i, op1, op2)))
			else:
				stack_.push(str(math_oper(i, op1, op2)))
	if stack_.size() > 1:
		raise PostfixFormatException("Too many operands")
	elif stack_.size() == 0:
		raise PostfixFormatException("Insufficient operands")
	
	result = stack_.pop()
	if is_int(result):
		return int(result)
	else:
		return float(result)


def valid_ints(n1, n2):
	""" Returns True if both inputs are integer numbers, False - otherwise"""
	return is_int(n1) and is_int(n2)

def is_number(s) :
	""" Returns True if string is a number """
	try:
		float(s)
		return True
	except ValueError: 
		return False

def is_int(s):
	""" Returns True if string is an int. """
	try:
		int(s)
		return True
	except ValueError:
		return False

def is_operator(s):
	"""Unpacking dictionary keys into a list"""
	keys = [*Dict.value]  #*
	if s in keys:
		return True
	else:
		return False


def math_oper(operator, val1, val2): 
	""" helper function for evaluating Math Expressions for postfix_eval function """
	'''operator is the operator, val1 is the first operand, val2 is the second operand'''
	if valid_ints(val1, val2):
		val1 = int(val1)
		val2 = int(val2)
	else: # cast to float
		val1 = float(val1)
		val2 = float(val2)

	if operator == '*':
		return  val2 * val1
	elif operator == '-':
		return  val2 - val1
	elif operator == '/':
		if val1 == 0:
			raise ValueError
		else: 
			return (val2 / val1)
	elif operator == '+':
		return  val2 + val1
	elif operator == '<<':  
		return val2*(2**val1)
	elif operator == '>>':
		return val2//(2**val1) 
	else: #operator == "**"
		return (val2**val1)


def prefix_to_postfix(input_str): 
	"""Converts a prefix expression to an equivalent postfix expression"""
	"""Input argument: a string containing a prefix expression where tokens are 
	space separated. Tokens are either operators + - * / ^ parentheses ( ) or numbers
	Returns a String containing a postfix expression(tokens are space separated)"""

	""" Tests to see if the given Postfix Expression is a solvable and valid postfix expression"""
	stack_ = Stack(30)
	# split and reverse list
	inp_list = input_str.split()[::-1]
	if inp_list is None:
		raise PostfixFormatException("Insufficient operands")
	keys = [*Dict.value]
	for i in inp_list:
		if i not in keys: #value not in ('*','-','/','+','**', '>>', '<<')
			if is_number(i):
				stack_.push(i)
			else:
				raise PostfixFormatException("Invalid token")
		else: #operator encountered ('*','-','/','+','**', '>>', '<<')
			if stack_.size() < 2:
				raise PostfixFormatException("Insufficient operands")
			op1 = stack_.pop() 
			op2 = stack_.pop()
			# both numbers but we need to check if both are ints for '<<' and '>>'
			if i not in [">>", "<<"] or valid_ints(op1,op2) == True:
				stack_.push( str(op1)+ " " + str(op2) + " " + str(i))
			else:
				raise PostfixFormatException("Illegal bit shift operand")
	
	if stack_.size() > 1:
		raise PostfixFormatException("Too many operands")
	elif stack_.size() == 0:
		raise PostfixFormatException("Insufficient operands")

	return stack_.pop() #remaining result of the long string 












