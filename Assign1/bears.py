def bears(n):
	if (n <= 42):
		return (n==42)

	elif (n%5 ==0):
		return (n-42)

	elif (n%2 ==0):
		return (n/2)

	else:
		if (n%3 == 0 or n%4 == 0):
			return (bears(n - (n % 10) * (n // 10 % 10)))

			