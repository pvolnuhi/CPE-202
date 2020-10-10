#def h(x):
#	z = x +1
#	return z+2
	#print(z+2)
#z = 4
#print(z+2)
#y = h(8)

#print(z+2)

#def g(x):
#	x = 9
#	return x + 3
#x = 4
#x = g(x)

#print(x + 3)

# class P:
# 	def __init__(self,x):
# 		self.x = x
# 		# ...
# y = P(9)
# z = y
# x = P(9)
# w = 9

# def scramble(a, b):
# 	b += 8
# 	a.x += 8

# scramble(z, w)

# print(y.x, z.x, x.x, w)


def g(empty_queue):

	q = empty_queue()
	for i in range(6):
		q = enqueue(q, i+1)
	for i in range(3):
		val, q = dequeue(q)
		val, q = dequeue(q)
		q = enqueue(q, val)

	val, q = dequeue(q)
	print(val)