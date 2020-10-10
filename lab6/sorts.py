import random
import time

# def main():
# 	# Give the random number generator a seed, so the same sequence of 
# 	# random numbers is generated at each run
# 	random.seed(1234) 
	
# 	# Generate 5000 random numbers from 0 to 999,999
# 	randoms = random.sample(range(1000000), 100000)
# 	start_time = time.time() 
# 	comps = insertion_sort(randoms)
# 	stop_time = time.time()
# 	print(comps, stop_time - start_time)

def selection_sort(alist):
	comps = 0
	for i in range(0, len(alist)-1): #len(alist)-1
		min_index = i
		for j in range(i+1, len(alist)):
			comps += 1
			if alist[min_index] > alist[j]:
				min_index = j
		if min_index != i: # swapping 
			alist[i], alist[min_index] = alist[min_index], alist[i]  # a,b = b,a swap 
	return comps
	
def insertion_sort(alist): # how to incorporate comparison counter? 
	comps = 0
	for index in range(1, len(alist)):
		curr_value = alist[index]
		pos = index
		while pos > 0:
			if curr_value < alist[pos-1]:
				comps +=1
				alist[pos] = alist[pos-1]
				alist[pos-1] = curr_value
				pos = pos-1
			else:
				comps += 1
				break
	return comps 


# if __name__ == '__main__': 
# 	main()

