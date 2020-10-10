#
#Polina Volnuhina
#014302388
#4/24/2019
#
#Assign2 
#CPE 202-13
#Testing for evaluations using precedence and left or right association of operations


import unittest     #one error is that i can't compute 5 >> 2
from exp_eval import * 

class test_expressions(unittest.TestCase):
		
	#tests infix_to_postfix conversion
	def test_infix_to_postfix(self):  #check how to handle negatives
		self.assertEqual(infix_to_postfix("3"), ("3"))
		self.assertEqual(infix_to_postfix("-3"), ("-3"))
		self.assertEqual(infix_to_postfix("6 - 3 + 2"), ("6 3 - 2 +"))
		self.assertEqual(infix_to_postfix("8 + 3"), ("8 3 +"))  
		self.assertEqual(infix_to_postfix("1 + 2 - 0"), ("1 2 + 0 -"))
		self.assertEqual(infix_to_postfix("-6 ** 0 ** 4.0"), ("-6 0 4.0 ** **"))
		self.assertEqual(infix_to_postfix("( ( 3 + 4 ) * 5 )"), ("3 4 + 5 *")) 
		self.assertEqual(infix_to_postfix("1 + 9 * 11"), ("1 9 11 * +"))
		self.assertEqual(infix_to_postfix("3 * ( 0.2 + 0.3 ) * 2"), ("3 0.2 0.3 + * 2 *"))
		self.assertEqual(infix_to_postfix("2 / ( 2 / 2 * ( 2 + 2 ) )"), ("2 2 2 / 2 2 + * /"))
		self.assertEqual(infix_to_postfix("0.0 ** ( 0.0 / ( 0.0 + 0.0 + 0.0 ) )"), ("0.0 0.0 0.0 0.0 + 0.0 + / **"))
		
	
	
	#returns calculated result, but need to account for error as well such as divisor being 0 
	def test_postfix_eval(self):
		self.assertAlmostEqual(postfix_eval("0 0.0 -"), (0.0))
		self.assertAlmostEqual(postfix_eval("3 0.2 0.3 + * 2 *"), (3.0))
		self.assertAlmostEqual(postfix_eval("10 0 +"), (10)) 

		with self.assertRaises(ValueError):
			postfix_eval("3 0 /")
		with self.assertRaises(ValueError): 
			postfix_eval("3 0.0 /")
		with self.assertRaises(ValueError): 
			postfix_eval("0.0 0.0 /")

	def test_postfix_eval_01(self): 
		self.assertAlmostEqual(postfix_eval("3 5 +"), (8))

	def test_postfix_eval_02(self):
		try:
			postfix_eval("blah")
			self.fail()
		except PostfixFormatException as e:
			self.assertEqual(str(e), ("Invalid token"))

	def test_postfix_eval_03(self):   
		try:
			postfix_eval("4 +") #size = 2 or 0 
			self.fail()
		except PostfixFormatException as e:
			self.assertEqual(str(e), ("Insufficient operands"))

	def test_postfix_eval_04(self):
		try:
			postfix_eval("1 2 3 +")
			self.fail()
		except PostfixFormatException as e:
			self.assertEqual(str(e), ("Too many operands"))

	def test_postfix_eval_05(self):
		try:
			postfix_eval("5 2.0 >>")
			self.fail()
		except PostfixFormatException as e:
			self.assertEqual(str(e), ("Illegal bit shift operand"))

	def test_postfix_eval_06(self):
		try:
			postfix_eval("5.0 2.0 <<")
			self.fail()
		except PostfixFormatException as e:
			self.assertEqual(str(e), ("Illegal bit shift operand"))

	def test_postfix_eval_07(self):
		try:
			postfix_eval("5 << 2.0")
			self.fail()
		except PostfixFormatException as e:
			self.assertEqual(str(e), ("Insufficient operands"))

	def test_postfix_eval_08(self):
		try:
			postfix_eval("5.0 << 2")
			self.fail()
		except PostfixFormatException as e:
			self.assertEqual(str(e), ("Insufficient operands"))

	def test_postfix_eval_09(self):
		try:
			postfix_eval(" ") #line 75 
			self.fail()
		except PostfixFormatException as e:
			self.assertEqual(str(e), ("Insufficient operands"))
			


	#needs to return string as well
	def test_prefix_to_postfix(self):  
		self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"),("3 2 1 / - 4 5 / 6 - *"))
		self.assertEqual(prefix_to_postfix("* - -3 / -2 1 - / 4 5 6"),("-3 -2 1 / - 4 5 / 6 - *"))
		self.assertEqual(prefix_to_postfix("* + 4 / 2 7 + / 8 1 1"), ("4 2 7 / + 8 1 / 1 + *"))
		self.assertEqual(prefix_to_postfix("* + 4 >> 2 7 + >> 8 1 1"), ("4 2 7 >> + 8 1 >> 1 + *"))





if __name__ == "__main__":
	unittest.main()
